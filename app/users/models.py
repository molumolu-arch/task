from django.db import models
from django.contrib.auth.models import AbstractUser


from django.utils import timezone 

class User(AbstractUser):
    coins = models.IntegerField(default=0)
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique = True)
    REQUIRED_FIELDS = ['email']

   
class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduled_rewards')
    amount = models.IntegerField()
    execute_at = models.DateTimeField()

    class Meta:
        ordering = ['execute_at']

    def __str__(self):
        return f"Scheduled {self.amount} for {self.user.username} at {self.execute_at}"


class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward_logs')
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-given_at']

    def __str__(self):
        return f"Reward of {self.amount} given to {self.user.username} at {self.given_at}"


class RewardRequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward_requests')
    requested_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-requested_at']

    def __str__(self):
        return f"Request by {self.user.username} at {self.requested_at}"