from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.urls import path
from django.template.response import TemplateResponse

User = get_user_model()

class CustomAdminSite(AdminSite):
    site_header = "RegionWeb Admin"
    site_title = "RegionWeb Admin Portal"
    index_title = "Welcome to RegionWeb Dashboard"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('stats/', self.admin_view(self.stats_view), name="stats"),
        ]
        return custom_urls + urls

    def stats_view(self, request):
        context = dict(
            self.each_context(request),
            title='Site Stats',
            total_users=User.objects.count(),
        )
        return TemplateResponse(request, "admin/stats.html", context)

custom_admin_site = CustomAdminSite(name='custom_admin')