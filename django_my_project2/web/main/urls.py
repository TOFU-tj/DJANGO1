from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.about_page, name='about'), 
    path('merch/', views.merch_page, name='merch'), 
    path('contacts/', views.contact_page, name='con'), 
]
