from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User

class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('email', 'password','username' )}),
      (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (('user_info'), {'fields': ('coins',)}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('username','email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'is_staff', "coins"]
  search_fields = ('email', 'username')
  ordering = ('email', )
  
admin.site.register(User, UserAdmin)

