from django.contrib import admin
from .models import UserInfo,CustomUser

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass