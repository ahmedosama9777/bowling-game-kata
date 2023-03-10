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

        self.assertEqual(str(e.exception), "Pins can't be less than nor equal to 0.")

    def test_roll_greater_than_ten(self):
        with self.assertRaises(ValueError) as e:
            self.game.roll(11)

        self.assertEqual(str(e.exception), "Pins can't be greater than 10.")

    def test_all_ones_game(self):
        for _ in range(20):
            self.game.roll(1)

        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        self.game.roll(8)
        self.game.roll(2)
        self.game.roll(3)

        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)

        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        for _ in range(12):
            self.game.roll(10)

        self.assertEqual(self.game.score(), 300)
