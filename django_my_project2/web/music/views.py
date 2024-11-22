from django.shortcuts import render
from .models import Music

def music_page(request): 
    music = Music.objects.order_by('-date')
    return render(request, 'music/music_page.html', {'music' : music})