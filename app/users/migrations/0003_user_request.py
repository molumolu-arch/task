# Generated by Django 5.2.2 on 2025-06-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rewardlog_scheduledreward'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='request',
            field=models.BooleanField(default=True),
        ),
    ]
