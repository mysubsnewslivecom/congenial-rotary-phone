from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets

from main.api import serializers
from main.movieflex.models import Media, Watching

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class MediaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MediaSerializer
    queryset = Media.objects.all()


class WatchingViewset(viewsets.ModelViewSet):
    serializer_class = serializers.WatchingSerializer
    queryset = Watching.objects.all()
