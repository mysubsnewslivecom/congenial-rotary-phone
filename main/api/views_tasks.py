from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets

from main.api import serializers
from main.tasks.models import Todo

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class TodoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.all()


