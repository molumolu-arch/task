from django.db import models
from users.models import User
from .tasks import process_reward

class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduled_rewards')
    amount = models.PositiveIntegerField(default=0)
    execute_at = models.DateTimeField()

    class Meta:
        ordering = ['execute_at']
    
    def save(self, *args, **kwargs):
        super(ScheduledReward, self).save(*args,**kwargs)
        process_reward.apply_async(args=[self.user.id, self.amount], eta = self.execute_at)



class RewardLog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward_logs')
    amount = models.PositiveIntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-given_at']


class RewardRequestLog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward_requests')
    requested_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-requested_at']

