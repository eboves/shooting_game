from turtle import Screen
from score_board import Score_board
from monter_manager import MonsterManager
from player import Player
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()