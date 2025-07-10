from django.urls import path
from .views import register, login, profile_view, logout_view, home

urlpatterns = [
    path('', home, name='home'),  # <--- правильный путь для /
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/view/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout'),
]