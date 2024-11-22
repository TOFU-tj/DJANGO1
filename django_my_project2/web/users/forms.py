from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя пользователя',
        }),
        help_text=None  # Убираем help_text для имени пользователя
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Введите ваше имя пользователя'
        }),
        help_text=None  # Убираем help_text для имени пользователя
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш пароль'
        }),
        help_text=None  # Убираем help_text для пароля
    )
