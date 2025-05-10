from django.urls import path
from . import auth as auth_views, views

urlpatterns = [
    path('login/', auth_views.login_view, name='login'),
    path('signup/', auth_views.signup_view, name='signup'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('forbidden/', views.forbidden, name='forbidden'),
]
