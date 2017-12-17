import boardgamegeek as bgg
import json
import os

from gamelib.criteria import *

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def load_obj(clazz, filename):
    path = os.path.join(__location__, filename)
    with open(path, 'r') as file:
        data = json.load(file)
        return clazz(data)

sample_game = load_obj(bgg.objects.games.BoardGame, 'sample_game.json')

def test_number_players():
    pass
