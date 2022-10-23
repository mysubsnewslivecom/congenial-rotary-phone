from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics
from rest_framework.response import Response

from main.api import serializers
from main.utility.functions import Ipify

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class IpifyAPI(generics.GenericAPIView):
    serializer_class = serializers.IpifySerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        ip = Ipify().get_ipify()
        serializer = self.serializer_class(ip)
        return Response(data=serializer.data)
