from __future__ import absolute_import, unicode_literals
from users.models import User
from celery import shared_task

@shared_task
def process_reward(user_id, amount):

    from .models import RewardLog
    user = User.objects.get(id=user_id)
    user.coins += amount
    user.save()
    log = RewardLog.objects.create(user=user,amount=amount)



