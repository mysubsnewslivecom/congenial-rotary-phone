from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets
from rest_framework.response import Response

from main.api import serializers
from main.tasks.models import Todo
from main.utility.functions import LoggingService

log = LoggingService()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class TodoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()

    def list(self, request, *args, **kwargs):
        # super().retrieve(request, *args, **kwargs)
        data = Todo.objects.filter(is_active=True)
        log.info(list(data))
        return Response(list(data.values()))
