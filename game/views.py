from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Player, Game
from .game_logic import roll_dice
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to Snake and Ladder Game!")

def start_game(request):
    player1 = Player.objects.create(name="Player 1")
    player2 = Player.objects.create(name="Player 2")
    game = Game.objects.create()
    game.players.add(player1, player2)
    game.save()
    return JsonResponse({"message": "Game started", "game_id": game.id})

def roll_dice_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if game.game_over:
        return JsonResponse({"message": "Game Over"})
    
    current_player = game.players.all()[game.current_turn]
    message = roll_dice(current_player, game)
    return JsonResponse({"message": message})

def get_game_state(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    players = {player.name: player.position for player in game.players.all()}
    return JsonResponse({"players": players, "game_over": game.game_over})

def roll_dice(request, game_id):
    game = Game.objects.get(pk=game_id)
    result = game.roll_dice()  # Implement this method in your Game model
    return JsonResponse({"message": result})