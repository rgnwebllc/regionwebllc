from django.contrib import admin
from config.admin_site import custom_admin_site
from .models import *

@admin.register(Testimonial, site=custom_admin_site)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'quote')

@admin.register(Lead, site=custom_admin_site)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at')