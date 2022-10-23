from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets

from main.api import serializers
from main.gitsvn.models import ProjectDetail

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class ProjectDetailAPI(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectDetailSerializer
    queryset = ProjectDetail.objects.all()

    # def get(self, request, *args, **kwargs):
