import random
from .models import Player, Game

SNAKES = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def move_position(position):
    if position in SNAKES:
        return SNAKES[position]
    elif position in LADDERS:
        return LADDERS[position]
    return position

def roll_dice(player, game):
    dice_value = random.randint(1, 6)
    player.position += dice_value
    player.position = move_position(player.position)
    
    if player.position >= 100:
        game.game_over = True
        player.position = 100
        return f"{player.name} wins!"
    
    game.current_turn = (game.current_turn + 1) % game.players.count()
    game.save()
    player.save()
    return f"{player.name} rolled a {dice_value} and moved to {player.position}"
