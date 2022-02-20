import imp
from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name='home'),
]