from rest_framework import serializers

from main.gitsvn.models import ProjectDetail


class OpenWeatherSerializer(serializers.Serializer):
    main = serializers.JSONField()
    weather = serializers.JSONField()
    name = serializers.CharField()
    sys = serializers.JSONField()
    cod = serializers.IntegerField()
    coord = serializers.JSONField()
    wind = serializers.JSONField()


class IpifySerializer(serializers.Serializer):
    ip = serializers.JSONField()


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = (
            "name",
            "project_id",
            "url",
            "git",
            "namespace",
            "default_branch",
            "ssh_url_to_repo",
        )
