"""

"""
from model.game import SplendorGame
from model.player import SplendorPlayer
from unittest import TestCase

class GameTest(TestCase):
    """
    """
    
    def test_game_creation(self):
        game = SplendorGame()
        self.assertTrue(True)
    
    def test_game_initialization(self):
        game = SplendorGame()
        
        
        self.assertTrue(isinstance(game.players, list))
        for player in game.players:
            self.assertTrue(isinstance(player, SplendorPlayer))