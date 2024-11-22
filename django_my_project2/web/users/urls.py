from . import views
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('login', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.registration, name='registration')
]
