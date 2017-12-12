import boardgamegeek as bgg
from pprint import pprint

from gamelib import criteria, stats

TTL = 15 * 60
USER = 'ungood'

# Cache BGG requests for 15 minutes
cache = bgg.CacheBackendSqlite('cache.db', TTL)
client = bgg.BGGClient(cache=cache)

#pprint(client.game('Railways of the World').data())

lunchtime = criteria.MaxPlaytime(45)
three = criteria.NumberPlayers(3)

def players(min, max):
    for players in range(min, max+1):
        yield criteria.NumberPlayers(3)
    
    
lunch_games = stats.Group('Board Game Lunch',
    [criteria.MaxPlaytime(45)],
    players(2, 6))

for bucket in lunch_games.buckets:
    print(bucket)

#scores = []
#for user_game in client.collection(USER, own=True):
#    game = client.game(game_id=user_game.id)
#    scores.append(bucket.score(game))

#for score in reversed(sorted(scores)):
#    print(score)