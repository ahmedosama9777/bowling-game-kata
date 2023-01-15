class Game():
    def score(self):
        return 0
    
    def roll(self, pins: int):
        if pins <= 0:
            raise ValueError("Pins can't be less than 0.")
        elif pins >= 10:
            raise ValueError("Pins can't be greater than 10.")
    