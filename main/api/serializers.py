from django_celery_results.models import TaskResult
from rest_framework import serializers

from main.gitsvn.models import ProjectDetail
from main.health.models import DailyTracker, Rule
from main.movieflex.models import Media, Watching


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


class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ("name", "is_active")


class DailyTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTracker
        fields = ("date", "status", "id", "rule_id")
        lookup_field = "date"


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ("id", "name", "category", "sub_category")


class WatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watching
        fields = "__all__"


class TriggerHealthSerializer(serializers.Serializer):
    uuid = None


class CeleryTaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ("task_id", "status", "result", "date_done")
