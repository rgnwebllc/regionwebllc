from django.urls import path
from django.shortcuts import redirect
from . import auth as auth_views
from .views import dashboard_view

urlpatterns = [
    path('', lambda request: redirect('login')),  # 👈 redirect base /accounts/ to login
    path('dashboard/', dashboard_view, name='dashboard'),
    path('signup/', auth_views.signup_view, name='signup'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
]