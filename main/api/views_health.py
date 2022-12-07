from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.vary import vary_on_cookie
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from main.api import serializers
from main.health.models import DailyTracker, Rule
from main.health.tasks import trigger_actions
from main.home.mixins import AuditMixins
from main.utility.functions import LoggingService
from main.utility.mixins import EnablePartialUpdateMixin

log = LoggingService()


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class RuleAPI(viewsets.ModelViewSet):
    serializer_class = serializers.RulesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Rule.objects.all()


class DailyActivityViewset(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = DailyTracker.objects.all()
    serializer_class = serializers.DailyTrackerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "date"
    http_method_names = ["get", "patch"]

    # @action(detail=False, methods=['get'], url_path='gdt', name='Get daily status')
    @action(detail=False, url_path="gdt", methods=["get"], name="Get daily status")
    @method_decorator(never_cache)
    @method_decorator(vary_on_cookie)
    def get_daily_status(self, request, *args, **kwargs):
        data = DailyTracker.objects.get_daily_status()
        return Response(data=data)

    @method_decorator(never_cache)
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        date = kwargs["date"]
        # data = Rule.objects.filter(date=date).values()
        data = list(DailyTracker.objects.filter(date=date).select_related("rule_id"))
        data_arr = list()
        for d in data:
            # data_dict = dict()
            data_dict = {
                "name": d.rule_id.name,
                "id": d.id,
                "status": d.status,
                "date": d.date,
            }
            data_arr.append(data_dict)
        return Response(data_arr)

    def update(self, request, pk=None, *args, **kwargs):

        data = request.data
        id = data["id"]
        data_status = data["status"]
        result = DailyTracker.objects.filter(id=id).update(status=data_status)
        message = {"message": f"{result} record updated."}

        return Response(data=message, status=status.HTTP_202_ACCEPTED)


class TriggerHealth(AuditMixins, viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.TriggerHealthSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        audit = dict()
        audit["task_id"] = self.generate_uuid()
        self.info("TriggerHealth Action tiggered.", **audit)
        task_id = trigger_actions.delay(**audit)
        audit["celery_task_id"] = str(task_id)
        self.info("TriggerHealth Celery tasks tiggered.", **audit)
        log.info(f"{str(task_id) = }")
        return Response({"task_id": str(task_id), "message": "Task triggered"})

    def list(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
