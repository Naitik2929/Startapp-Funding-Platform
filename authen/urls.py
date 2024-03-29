from django.urls import path
from . import views

app_name = "authen"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('about', views.about_view, name='about'),
]