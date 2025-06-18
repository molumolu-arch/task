from .views import RewardLogView, RequestRewardReview
from django.urls import path

urlpatterns = [
    path("rewards/", RewardLogView.as_view(), name= "rewards_view"),
    path("request/", RequestRewardReview.as_view(), name= "rewards_request_view"),
]