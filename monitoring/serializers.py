from rest_framework import serializers
from .models import StatusCheckResult


class StatusCheckResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCheckResult
        fields = "__all__"
