class Game():
    def __init__(self):
        self.total_score = 0
    def score(self):
        return self.total_score
    
    def roll(self, pins: int):
        if pins <= 0:
            raise ValueError("Pins can't be less than 0.")
        elif pins >= 10:
            raise ValueError("Pins can't be greater than 10.")

        self.total_score += pins