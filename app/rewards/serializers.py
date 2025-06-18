from rest_framework import serializers
from .models import RewardLog

class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ["user","amount","given_at"]