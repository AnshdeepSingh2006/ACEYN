from django.shortcuts import render
from django.http import HttpResponse
from .models import NewGame


def home(request):
    newgames = NewGame.objects.all()
    return render(request, 'home.html', {'games': newgames})
