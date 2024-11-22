from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.music_page, name='music' ), 
]
