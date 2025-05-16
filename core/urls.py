from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('features/', views.features_view, name='features'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
    path('free-consultation/', views.consultation_view, name='consultation'),
    path('contact/', views.consultation_request, name='consultation-request'),
    path('log-to-discord/', views.forward_log_to_discord, name='log_to_discord'),
]