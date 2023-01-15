class Game():
    def __init__(self):
        self.total_score = 0
        self.current_frame = []
        self.bonus = False

    def _validate_pins(self, pins: int):
        if pins <= 0:
            raise ValueError("Pins can't be less than 0.")
        elif pins >= 10:
            raise ValueError("Pins can't be greater than 10.")
            
    def score(self) -> int:
        return self.total_score
    
    def roll(self, pins: int):
        self._validate_pins(pins)

        self.total_score += pins
        if self.bonus:
            self.bonus = False
            self.total_score += pins

        if len(self.current_frame) < 2:
            self.current_frame.append(pins)
        
        if sum(self.current_frame) == 10:
            self.bonus = True

        if len(self.current_frame) == 2:
            self.current_frame = []
    
    