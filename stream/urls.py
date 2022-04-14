import imp
from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('register/', views.registerPage, name="register"),
    path('show/<str:pk>/', views.show, name='show'),
    path('production/<str:pk>/', views.production, name='production'),
    # path('/<str:pk>/', views.production, name='production'),
    path('watchlist/', views.watchlist, name="watchlist"),
    # path('watchlist-add/<str:pk>/', views.watchlistAdd, name='watchlist-add')

    # watchlist-add

    path('', views.home, name='home'),
]