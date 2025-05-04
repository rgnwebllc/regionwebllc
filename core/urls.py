from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('pricing/', views.pricing_view, name='pricing'),
]