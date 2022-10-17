from rest_framework import serializers

class OpenWeatherSerializer(serializers.Serializer):
    main = serializers.JSONField()
    weather = serializers.JSONField()
    name = serializers.CharField()
    sys = serializers.JSONField()
    cod = serializers.IntegerField()
    coord = serializers.JSONField()
    wind = serializers.JSONField()
