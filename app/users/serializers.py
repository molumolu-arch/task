from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, RewardLog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',"email","coins"]

class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = '__all__'