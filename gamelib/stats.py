import itertools
import functools
import operator
        
class Score(object):
    def __lt__(self, other):
        return self.score < other.score
        
class CriteriaScore(Score):
    def __init__(self, game, criteria):
        self.game = game
        self.score = criteria.score(game)
    
    def __str__(self):
        return '{: 3.0%} - {}'.format(self.score, self.game.name)
        
class GameBucketScore(Score):
    def __init__(self, game, bucket):
        self.game = game
        self.bucket = bucket
        self.scores = [CriteriaScore(game, c) for c in bucket.criteria]
        criteria_score = functools.reduce(operator.mul, [c.score for c in self.scores], 1.)
        game_score = game.rating_bayes_average
        self.score = game_score * criteria_score
        
    def __str__(self):
        return "{:01.2f} - {}".format(self.score, self.game.name)

class Bucket(object):
    def __init__(self, *criteria):
        self.criteria = criteria
        
    def score(self, game):
        return GameBucketScore(game, self)
        
    def __str__(self):
        return ', '.join(str(c) for c in self.criteria)

class Group(object):
    def __init__(self, name, *criteria_iterables):
        self.name = name
        self.buckets = []
        for criteria in itertools.product(*criteria_iterables):
            self.buckets.append(Bucket(criteria))