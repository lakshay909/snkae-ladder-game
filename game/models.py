from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField(default=0)

class Game(models.Model):
    players = models.ManyToManyField(Player)
    current_turn = models.IntegerField(default=0)
    game_over = models.BooleanField(default=False)
