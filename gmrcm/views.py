from django.shortcuts import render
from django.http import HttpResponse
from .models import Games3, Games2, Games1


# game recommended home page

def index(request):
    return render(request, 'gmrcm.html')


# game1-adventure games
def adventure_games(request):
    games1 = Games1.objects.all()
    return render(request, 'adventure.html', {'games': games1})

# game-2


def action_games(request):
    games2 = Games2.objects.all()
    return render(request, 'action.html', {'games': games2})

# game-3


def strategy_games(request):
    games3 = Games3.objects.all()
    return render(request, 'strategy.html', {'games': games3})




