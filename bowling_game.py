class Game():
    def score(self):
        return 0
    
    def roll(self, pins: int):
        if pins < 0:
            raise ValueError("Pins must be equal or greater than 0.")