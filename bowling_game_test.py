from unittest import TestCase

from bowling_game import Game

class TestBowlingGame(TestCase):
    def test_create_game(self):
        game = Game()
        self.assertEqual(game.score(), 0)