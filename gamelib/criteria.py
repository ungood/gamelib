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
class NumberPlayers(Criteria):
    def __init__(self, num_players):
        self.num_players = num_players
        
    def score(self, game):
        if game.minplayers > self.num_players or self.num_players > game.maxplayers:
            return 0.
        else:
            suggested = game.data()['suggested_numplayers']
            votes = int(suggested['total_votes'])
            results = suggested['results'][str(self.num_players)]
            score = (3 * results['best']) + (2 * results['recommended']) + results['not_recommended']
            return float(score) / (votes * 3)
            
    def __str__(self):
        return '{} players'.format(self.num_players)
        

class MaxPlaytime(Criteria):
    def __init__(self, max_playtime):
        self.max_playtime = max_playtime
    
    def score(self, game):
        mean = game.playingtime
        # An estimate for now.
        stddev = mean / 6.
        probability = norm.cdf(self.max_playtime, loc=mean, scale=stddev)
        return probability
    
    def __str__(self):
        return 'playtime < {}'.format(self.max_playtime)


class MinAge(Criteria):
    """
    Scores a game based on the probability that a player of the
    given age can play the game.
    """
    def __init__(self, min_age):
        pass
        
    def score(self, game):
        pass