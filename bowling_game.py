class Game():
    def __init__(self):
        self.total_score = 0
        self.current_frame = []
        self.stribe_bonus = 0
        self.strike_bonus = 0

    def _validate_pins(self, pins: int):
        if pins <= 0:
            raise ValueError("Pins can't be less than nor equal to 0.")
        elif pins > 10:
            raise ValueError("Pins can't be greater than 10.")

    def score(self) -> int:
        return self.total_score
    
    def roll(self, pins: int):
        self._validate_pins(pins)

        self.total_score += pins
        if self.stribe_bonus:
            self.stribe_bonus -= 1
            self.total_score += pins
        elif self.strike_bonus:
            self.strike_bonus -= 1
            self.total_score += pins

        if len(self.current_frame) < 2:
            self.current_frame.append(pins)
        
        if sum(self.current_frame) == 10 and len(self.current_frame) == 1:
            self.strike_bonus = 2
            self.current_frame = []
        elif sum(self.current_frame) == 10:
            self.stribe_bonus = 1

        if len(self.current_frame) == 2:
            self.current_frame = []
    
    