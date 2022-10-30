from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets
from rest_framework.response import Response

from main.api import serializers
from main.health.models import Rule

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class RuleAPI(viewsets.ModelViewSet):
    serializer_class = serializers.RulesSerializer
    queryset = Rule.objects.all()
