from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from main.api import serializers
from main.health.models import Rule, DailyTracker
from rest_framework.decorators import action
from main.utility.functions import LoggingService
from rest_framework.response import Response

log = LoggingService()


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


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
    @action(detail=False, url_path='gdt', methods=['get'], name='Get daily status')
    def get_daily_status(self, request, *args, **kwargs):
        data = DailyTracker.objects.get_daily_status()
        log.debug(f"{data = }")
        return Response(data=data)

    def retrieve(self, request, *args, **kwargs):
        date = kwargs["date"]
        data = Rule.objects.filter(rules__date=date)
        log.info(data)
        # data = Rule.objects.filter(rules__date=date).values_list("name", flat=True)
        # data = DailyTracker.objects.filter(date=date).values()
        return Response(data.values())
