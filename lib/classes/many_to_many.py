class Game:
    def __init__(self, title):
        self.title = title
        self._results = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) == str and len(value) > 0:
            self._title = value 

    def results(self):
        return self._results

    def players(self):
        return list({result.player for result in self._results})

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        if scores:
            return sum(scores) / len(scores)


class Player:
    def __init__(self, username):
        self.username = username
        self._results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if type(value) == str and 2 <= len(value) <= 16:
            self._username = value

    def results(self):
        return self._results

    def games_played(self):
        return list({result.game for result in self._results})

    def played_game(self, game):
        played = [result.game for result in self._results if result.game == game]
        if played:
            return True
        else:
            return False 

    def num_times_played(self, game):
            return len([result for result in self._results if result.game == game])

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score 
        game._results.append(self)
        player._results.append(self)
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, "score"):
            return "Unable to change title"
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score