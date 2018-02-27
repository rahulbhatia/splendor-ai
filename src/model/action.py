"""
SplendorActions
"""
import logging

from copy import deepcopy
from itertools import combinations

logger = logging.getLogger(__name__)

class SplendorAction():
    def __init__(self):
        pass

    def transform(self, game_state):
        """
        Return a new Splendor Game with the state representing the new game
        """
        raise NotImplementedError("This is an abstract action")


class GemAction(SplendorAction):
    @classmethod
    def possibilities(cls, game_state):
        combos_3 = combinations(game_state.bank.stacks.keys(), 3)

        def construct_action(color_tuple, bank):
            valid_colors = []

            # Check if that color has any jewels
            for item in color_tuple:
                if bank.stacks[item].count > 0:
                    valid_colors.append(item)

            return GemAction(d_red=-1 if "RED" in valid_colors else 0,
                             d_blue=-1 if "BLUE" in valid_colors else 0,
                             d_green=-1 if "GREEN" in valid_colors else 0,
                             d_white=-1 if "WHITE" in valid_colors else 0,
                             d_black=-1 if "BLACK" in valid_colors else 0)

        actions = set()
        for combo in combos_3:
            actions.add(construct_action(combo, game_state.bank))

        ## Construct the Actions for the Double Token Take
        for color, stack in game_state.bank.stacks.items():
            if stack.count > 3:
                actions.add(GemAction(d_red=-2 if color == "RED" else 0,
                                      d_blue=-2 if color == "BLUE" else 0,
                                      d_green=-2 if color == "GREEN" else 0,
                                      d_white=-2 if color == "WHITE" else 0,
                                      d_black=-2 if color == "BLACK" else 0))

        return actions


    def __init__(self, d_red=0, d_green=0, d_blue=0, d_white=0, d_black=0):
        assert (d_red + d_green + d_blue + d_black + d_white) <= 3
        self.d_red = d_red
        self.d_blue = d_blue
        self.d_green = d_green
        self.d_white = d_white
        self.d_black = d_black

    def __repr__(self):
        return(f"GemAction({self.d_red},{self.d_blue},{self.d_green},{self.d_white},{self.d_black})")

    def __hash__(self):
        tup = (self.d_red, self.d_blue, self.d_green, self.d_white, self.d_black)
        return hash(tup)

    def __eq__(self, other):
        if self.d_red != other.d_red:
            return False
        elif self.d_blue != other.d_blue:
            return False
        elif self.d_green != other.d_green:
            return False
        elif self.d_white != other.d_white:
            return False
        elif self.d_black != other.d_black:
            return False
        else: return True

    def transform(self, game_state):
        """
        """
        updated_game = deepcopy(game_state)

        self._adjust_bank(updated_game.bank.stacks)
        self._adjust_player(updated_game.players[updated_game.current_player].bank.stacks)
        updated_game.current_player = (game_state.current_player + 1) % len(game_state.players)

        return updated_game

    def _adjust_bank(self, stacks):
        #Remove the money from the Bank
        stacks['RED'].count += self.d_red
        stacks['GREEN'].count += self.d_green
        stacks['BLUE'].count += self.d_blue
        stacks['WHITE'].count += self.d_white
        stacks['BLACK'].count += self.d_black

    def _adjust_player(self, stacks):
        #Remove Add Money to the Player
        stacks['RED'].count -= self.d_red
        stacks['GREEN'].count -= self.d_green
        stacks['BLUE'].count -= self.d_blue
        stacks['WHITE'].count -= self.d_white
        stacks['BLACK'].count -= self.d_black

class PurchaseAction(SplendorAction):
    def transform(self, game_state):
        """
        """
        raise NotImplementedError
