# Generated by Django 5.2.2 on 2025-06-11 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rewardrequestlog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rewardlog',
            options={'ordering': ['-given_at']},
        ),
        migrations.AlterModelOptions(
            name='scheduledreward',
            options={'ordering': ['execute_at']},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='request',
        ),
        migrations.AlterField(
            model_name='rewardlog',
            name='given_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rewardlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rewardrequestlog',
            name='requested_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rewardrequestlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scheduledreward',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_rewards', to=settings.AUTH_USER_MODEL),
        ),
    ]
