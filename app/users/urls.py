from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import ProfileView, RewardLogView, RequestRewardReview
from django.urls import path

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name= "token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name = "token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name = "token_verify" ),
    path("profile/", ProfileView.as_view(), name = "profile_view" ),
    path("rewards/", RewardLogView.as_view(), name= "rewards_view"),
    path("request/", RequestRewardReview.as_view(), name= "rewards_request_view"),
]