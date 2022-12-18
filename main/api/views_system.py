from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets

from main.api import serializers
from main.system.models import SystemProperty
from main.utility.functions import LoggingService

log = LoggingService()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class SystemPropertyViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SystemPropertySerializer
    queryset = SystemProperty.objects.all()
    lookup_field = "name"
