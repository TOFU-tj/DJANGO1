# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    image = models.ImageField(upload_to='user_images', blank=True, null=True)  # Убедитесь, что поле может быть пустым

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
