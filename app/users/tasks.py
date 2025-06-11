from __future__ import absolute_import, unicode_literals
from .models import ScheduledReward, RewardLog, RewardRequestLog
from django.utils import timezone
from celery import shared_task
from app.celery import app
from celery.schedules import crontab

@shared_task
def process_reward(reward_id):
    reward = ScheduledReward.objects.get(id=reward_id)
    user = reward.user
    user.coins += reward.amount
    user.save()
    log = RewardLog.objects.create(user=user,amount=reward.amount,given_at=timezone.now())



