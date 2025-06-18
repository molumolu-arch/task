from django.contrib import admin
from .models import ScheduledReward, RewardRequestLog, RewardLog

class ScheduledRewardAdmin(admin.ModelAdmin):
    readonly_fields = ('execute_at','user','amount')

class RewardRequestLogAdmin(admin.ModelAdmin):
    readonly_fields = ('requested_at','user')

class RewardLogAdmin(admin.ModelAdmin):
    readonly_fields = ('given_at','user','amount')

admin.site.register(ScheduledReward)
#admin.site.register(ScheduledReward, ScheduledRewardAdmin)
admin.site.register(RewardRequestLog, RewardRequestLogAdmin)
admin.site.register(RewardLog, RewardLogAdmin)

