from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect  
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  
                return redirect('home')  
            else:
                form.add_error(None, 'Неправильное имя пользователя или пароль.')
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})






def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)  # Не забудьте request.FILES для загрузки файлов
        if form.is_valid():
            form.save()  # Сохраняем пользователя
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')  # Перенаправление на страницу логина
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/registration.html', {'form': form})
    


    


def logout(request):
    return render(request, 'users/logout.html')
    
    
def profile(request):
    return render(request, 'users/profile.html') 
    
      
