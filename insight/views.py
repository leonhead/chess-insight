from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.paginator import Paginator
from .models import User, Game, Opening


def players(request):
    context = {
        'players': User.objects.all(),
    }
    return render(request, 'insight/players.html', context)

def player_details(request, player_id):
    player = get_object_or_404(User, id=player_id)
    context = {
        'player': player,
    }
    return render(request, 'insight/player_details.html', context)


def games(request):
    context = {
        'games': Game.objects.all(),
    }
    return render(request, 'insight/games.html', context)

def game_details(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    context = {
        'game': game,
        'players' : game.players.all()
    }
    return render(request, 'insight/game_details.html', context)

def openings(request):
    opening_list = Opening.objects.all()
    paginator = Paginator(opening_list, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'insight/openings.html', context)
