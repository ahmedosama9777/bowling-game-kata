class Game:
    def __init__(self):
        self.total_score = 0
        self.frames = []
        self.current_frame = []
        self.stribe_bonus = False
        self.strike_bonus = False

    def _validate_pins(self, pins: int):
        if pins <= 0:
            raise ValueError("Pins can't be less than nor equal to 0.")
        elif pins > 10:
            raise ValueError("Pins can't be greater than 10.")

    def _bonus_score(self, roll_index):
        if self.stribe_bonus:
            self.stribe_bonus = False
            if roll_index < len(self.frames) - 1:
                self.total_score += self.frames[roll_index + 1]
        elif self.strike_bonus:
            self.strike_bonus = False
            if roll_index < len(self.frames) - 2:
                self.total_score += (
                    self.frames[roll_index + 1] + self.frames[roll_index + 2]
                )

    def _is_bonus(self, pins):
        if len(self.current_frame) < 2:
            self.current_frame.append(pins)
        if sum(self.current_frame) == 10 and len(self.current_frame) == 1:
            self.strike_bonus += True
            self.current_frame = []
        elif sum(self.current_frame) == 10:
            self.stribe_bonus += True
        elif len(self.current_frame) == 2:
            self.current_frame = []

    def score(self) -> int:
        for roll_index in range(len(self.frames)):
            self.total_score += self.frames[roll_index]
            self._is_bonus(self.frames[roll_index])
            self._bonus_score(roll_index)
            if self.total_score == 300:
                break

        return self.total_score

    def roll(self, pins: int):
        self._validate_pins(pins)
        self.frames.append(pins)
