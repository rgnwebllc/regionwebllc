from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from config.admin_site import custom_admin_site

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {'fields': ('full_name', 'phone_number')}), 
    )

custom_admin_site.register(CustomUser, CustomUserAdmin)