from django.contrib import admin
from accounts.models import Profile, CurrentRestaurant
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(CurrentRestaurant)
class CurrentRestaurant(admin.ModelAdmin):
    list_display = ("get_full_name", )
class ProfileInline(admin.StackedInline):
      model = Profile
      can_delete= False
      extra=1

class UserAdmin(BaseUserAdmin):
	inlines=[ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


