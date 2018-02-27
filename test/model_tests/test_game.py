"""

"""


from model.action import *
from model.game import SplendorGame
from model.player import SplendorPlayer
from unittest import TestCase, skip

class GameTest(TestCase):
    """
    """

    def test_game_creation(self):
        """
        Can the game be created?
        """
        game = SplendorGame()
        self.assertTrue(True)

    def test_game_initialization(self):
        """
        Is the game created correctly?
        """
        game = SplendorGame()

        self.assertTrue(isinstance(game.players, list))
        for player in game.players:
            self.assertTrue(isinstance(player, SplendorPlayer))

    def test_game_starting_coin_override(self):
        """
        Given no coins in the bank, is the number of moves correct?
        """
        game = SplendorGame(starting_coin_ct=0)
        self.assertEquals(game.bank.stacks['RED'].count, 0)
        self.assertEquals(game.bank.stacks['GREEN'].count, 0)
        self.assertEquals(game.bank.stacks['BLUE'].count, 0)

    def test_game_available_moves(self):
        """
        Does the game have the right number of moves?
        """
        game = SplendorGame()
        moves = game.available_moves()
        self.assertEquals(len(moves), 15)


class GemActionTest(TestCase):
    def test_game_options(self):
        """
        Is the number of GemActions available correct?
        """
        game = SplendorGame()
        actions = GemAction.possibilities(game)
        self.assertEquals(len(actions), 15)

    def test_game_options_null_option(self):
        """
        Given no coins in the bank, is the number of moves correct?
        """
        game = SplendorGame(starting_coin_ct=0)
        actions = GemAction.possibilities(game)
        self.assertEquals(len(actions), 1)
        self.assertEqual(actions.pop(), GemAction(0,0,0,0,0))

    def test_game_update(self):
        """
        Can the game execute a GemAction
        """
        game = SplendorGame()
        action = GemAction(-1,-1,-1,0,0)
        updated_game = action.transform(game)
        updated = updated_game.bank.stacks
        for color in ["RED", "GREEN", "BLUE"]:
            self.assertEquals(updated[color].count, game.bank.stacks[color].count - 1)

        self.assertEquals(updated_game.current_player, 1)
