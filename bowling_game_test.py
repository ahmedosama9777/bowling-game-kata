from unittest import TestCase

from bowling_game import Game

class TestBowlingGame(TestCase):
    def setUp(self) -> None:
        self.game = Game()

    def test_create_game(self):
        self.assertEqual(self.game.score(), 0)
    
    def test_roll_negative_number(self):
        with self.assertRaises(ValueError) as e:
            self.game.roll(-1)
        
        self.assertEqual(str(e.exception), "Pins must be equal or greater than 0.")
