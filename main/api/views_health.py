from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from main.api import serializers
from main.health.models import DailyTracker, Rule
from main.health.tasks import trigger_actions
from main.utility.functions import LoggingService

log = LoggingService()


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class RuleAPI(viewsets.ModelViewSet):
    serializer_class = serializers.RulesSerializer
    queryset = Rule.objects.all()


class DailyActivityViewset(viewsets.ModelViewSet):
    queryset = DailyTracker.objects.all()
    serializer_class = serializers.DailyTrackerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "date"
    http_method_names = ["get"]

    # @action(detail=False, methods=['get'], url_path='gdt', name='Get daily status')
    # def get_daily_status(self, request, pk=None, *args, **kwargs):
    @action(detail=False, url_path="gdt", methods=["get"], name="Get daily status")
    @method_decorator(never_cache)
    # @method_decorator(cache_page(0))
    @method_decorator(vary_on_cookie)
    def get_daily_status(self, request, *args, **kwargs):
        data = DailyTracker.objects.get_daily_status()
        return Response(data=data)

    def retrieve(self, request, *args, **kwargs):
        date = kwargs["date"]
        data = Rule.objects.filter(rules__date=date).values()
        return Response(data)


class TriggerHealth(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # serializer_class = serializers.TriggerHealthSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        task_id = trigger_actions.delay()
        log.info(task_id)
        return Response({"task_id": str(task_id), "message": "Task triggered"})

    def list(self, request):
        return Response("list")

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
