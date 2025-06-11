from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ScheduledReward, RewardRequestLog

from .tasks import process_reward

@receiver(post_save, sender=ScheduledReward)
def schedule_reward(sender,instance,created, **kwargs):
    if created:
        eta = instance.execute_at
        process_reward.apply_async(args=[instance.id], eta=eta)
        

        
