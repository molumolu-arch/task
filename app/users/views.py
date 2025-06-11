from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .serializers import UserSerializer, RewardLogSerializer
from .models import RewardLog, RewardRequestLog, ScheduledReward
from django.utils import timezone
from datetime import timedelta

class ProfileView(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RewardLogView(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        logs = RewardLog.objects.filter(user=user)
        serializer = RewardLogSerializer(logs, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class RequestRewardReview(APIView):

    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        current_datetime = timezone.now()
        exec_time = current_datetime+timedelta(minutes=5)
        last_requested_log = RewardRequestLog.objects.filter(user=user).first()

        if last_requested_log:

            last_request = last_requested_log.requested_at.date()
            current_date = current_datetime.date()
            print(current_date, last_request)
            if last_request == current_date:
                return Response(
                    {"detail": "You have already requested your daily reward."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        ScheduledReward.objects.create(user=user,amount=100,execute_at=exec_time)
        RewardRequestLog.objects.create(user=user,requested_at=current_datetime)
        return Response(
                {"detail": "Reward request submitted successfully. U will get coins in 5 min."},
                status=status.HTTP_200_OK
            )