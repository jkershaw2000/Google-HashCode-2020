

class Book():
    def __init__(self, score):
        self.score = score

    def __str__(self):
        return ("Score: %d" % score)