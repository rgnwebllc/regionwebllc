from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('free-consultation/', views.consultation_view, name='consultation'),
    path('contact/', views.consultation_request, name='consultation-request'),
]