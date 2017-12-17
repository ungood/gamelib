from scipy.stats import norm

class Criteria(object):
    pass

# Rating (average + stddev)
# Criteria:
# number of players
# Age (minage)
# Weight
# Playtime (maxplaytime, minplaytime, playingtime
# "Tags" categories +  mechanics
# language_dependence

# 'minplayers': 2,
# 'maxplayers': 6,
# 'suggested_numplayers': {'results': {'1': {'best': 0,
#                                             'not_recommended': 109,
#                                             'recommended': 2},
#                                       '2': {'best': 6,
#                                             'not_recommended': 93,
#                                             'recommended': 51},
#                                       '3': {'best': 15,
#                                             'not_recommended': 41,
#                                             'recommended': 102},
#                                       '4': {'best': 74,
#                                             'not_recommended': 13,
#                                             'recommended': 84},
#                                       '5': {'best': 120,
#                                             'not_recommended': 1,
#                                             'recommended': 52},
#                                       '6': {'best': 72,
#                                             'not_recommended': 21,
#                                             'recommended': 65},
#                                       '6+': {'best': 3,
#                                              'not_recommended': 71,
#                                              'recommended': 3}},
#                           'total_votes': '197'},
def extract_player_score(game, num_players):
    suggested = game.data()['suggested_numplayers']
    votes = int(suggested['total_votes'])
    try:
        results = suggested['results'][str(num_players)]
    except KeyError:
        return None
    
    best = results['best']
    recommended = results['recommended']
    not_rec = results['not_recommended']
    neutral = votes - (best + recommended + not_rec)
    
    score = (best * 3) + (recommended * 2) + neutral
    return float(score) / (votes * 3)
    

class NumberPlayers(Criteria):
    def __init__(self, num_players):
        self.num_players = num_players
        
    def score(self, game):
        if game.minplayers > self.num_players or self.num_players > game.maxplayers:
            return 0.
        
        score = extract_player_score(game, self.num_players)
        return 0. if score is None else score
            
    def __str__(self):
        return '{} players'.format(self.num_players)

# 'maxplaytime': 180,
# 'minplaytime': 120,
# 'playingtime': 180,
class Playtime(Criteria):
    def __init__(self, max):
        self.max = max
    
    def score(self, game):        
        if game.minplaytime != game.maxplaytime:
            delta = (game.maxplaytime - game.minplaytime)
            mean = game.minplaytime + delta
            stddev = delta / 4.
        else:
            mean = game.playingtime
            stddev = mean / 6.
        
        probability = norm.cdf(self.max, loc=mean, scale=stddev)
        return probability
    
    def __str__(self):
        return 'playtime < {}'.format(self.max)


class MinAge(Criteria):
    """
    Scores a game based on the probability that a player of the
    given age can play the game.
    """
    def __init__(self, min_age):
        pass
        
    def score(self, game):
        pass
        

class Weight(Criteria):
    pass
    
# 'language_dependence': {'results': {
#     1: {'description': 'No necessary in-game '
#         'text',
#         'num_votes': 0},
#     2: {'description': 'Some necessary text - '
#         'easily memorized or '
#         'small crib sheet',
#         'num_votes': 12},
#     3: {'description': 'Moderate in-game text '
#         '- needs crib sheet or '
#         'paste ups',
#         'num_votes': 36},
#     4: {'description': 'Extensive use of text '
#         '- massive conversion '
#         'needed to be playable',
#         'num_votes': 1},
#     5: {'description': 'Unplayable in another '
#         'language',
#         'num_votes': 0}},
#    'total_votes': '49'},
class LanguageDependence(Criteria):
    def __init__(self, max_lang):
        self.max_leng = max_leng
    
    def score(self, game):
        pass
    
    def __str__(self):
        return "language dependence < {}".format(self.max_lang)


# 'mechanics': ['Action Point Allowance System',
#     'Auction/Bidding',
#     'Card Drafting',
#     'Pick-up and Deliver',
#     'Route/Network Building',
#     'Tile Placement'],
class Mechanic(Criteria):
    def __init__(self, mechanic):
        self.mechanic = mechanic
        
    def score(self, game):
        return 1. if mechanic in game.mechanics else 0.
    
    def __str__(self):
        return self.mechanic
        
# 'categories': ['Trains', 'Transportation', 'Video Game Theme'],        
class Category(Criteria):
    def __init__(self, category):
        self.category = category
    
    def score(self, game):
        return 1. if category in game.categories else 0.
    
    def __str__(self):
        return self.category
        