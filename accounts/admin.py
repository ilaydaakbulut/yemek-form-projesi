from django.contrib import admin
from accounts.models import Profile, CurrentRestaurant,Price,WorkType
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(Price)
admin.site.register(WorkType)

@admin.register(CurrentRestaurant)
class CurrentRestaurant(admin.ModelAdmin):

    list_display = ("get_full_name","created" )
    list_display_links = ["get_full_name","created"]
    list_filter=["created"]

class ProfileInline(admin.StackedInline):
      model = Profile
      can_delete= False
      extra=0
     
class UserAdmin(BaseUserAdmin):
	inlines=[ProfileInline]
	
admin.site.unregister(User)
admin.site.register(User, UserAdmin)