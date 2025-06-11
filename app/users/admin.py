from django.contrib import admin
from .models import User, ScheduledReward, RewardLog, RewardRequestLog
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User

class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('email', 'password','username' )}),
      (('Personal info'), {'fields': ('first_name', 'last_name')}),
      (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('user_info'), {'fields': ('coins',)}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('username','email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "coins"]
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )
  
admin.site.register(User, UserAdmin)

admin.site.register(ScheduledReward)
admin.site.register(RewardRequestLog)
admin.site.register(RewardLog)
