from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django_celery_results.models import TaskResult
from rest_framework import generics, viewsets
from rest_framework.response import Response

from main.api import serializers
from main.utility.functions import OpenWeather

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class OpenWeatherAPI(generics.GenericAPIView):
    # class OpenWeatherAPI(viewsets.GenericViewSet):

    serializer_class = serializers.OpenWeatherSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        location = request.query_params.get("q")
        if location is None:
            location = "Krakow"
        location = OpenWeather().get_weather(location=location)
        return Response(data=self.serializer_class(location).data)


class TaskResultViewset(viewsets.ModelViewSet):
    queryset = TaskResult.objects.all()
    serializer_class = serializers.CeleryTaskResultSerializer
    lookup_field = "task_id"
    http_method_names = ["get"]
