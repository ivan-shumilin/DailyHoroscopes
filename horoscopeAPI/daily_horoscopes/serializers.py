from rest_framework import serializers


class ForecastSerializer(serializers.Serializer):
    forecast = serializers.CharField(max_length=5000)