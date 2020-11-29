# Model for the Game's State Machine
#
#
import typing 

from model.action import *
from model.cards import SplendorDeck, SplendorCard
from model.money import SplendorBank
from model.player import SplendorPlayer


class SplendorGame():
    """
    This object represents the state of the game
    """
    def __init__(self, players=4, starting_coin_ct=7):
        self.turn = 0
        self.current_player = 0
        self.bank = SplendorBank(initial=starting_coin_ct)
        self.deck_low = SplendorDeck(level="low")
        self.deck_mid = SplendorDeck(level="mid")
        self.deck_high = SplendorDeck(level="high")
        self.table_low = [self.deck_low.draw() for i in range(4)]
        self.table_mid = [self.deck_mid.draw() for i in range(4)]
        self.table_high = [self.deck_high.draw() for i in range(4)]
        self.players = [SplendorPlayer(player) for player in range(players)]

    def __repr__(self):
        summary = "SPLENDOR GAME SUMMARY\n\n" \
            f"high: {self.table_high}\n" \
            f"mid:  {self.table_mid}\n" \
            f"low:  {self.table_low}\n" \
            f"{self.deck_high}\n" \
            f"{self.deck_mid}\n" \
            f"{self.deck_low}\n\n" \
            f"Bank    : {self.bank}\n\n"
        for i, player in enumerate(self.players):
            summary += f"{player}\n"

        return summary

    def available_moves(self):
        """
        Return all possible moves from this State
        """
        gem_actions = GemAction.possibilities(self)
        purchase_actions = PurchaseAction.possibilities(self)
        return gem_actions + purchase_actions

    def get_current_player(self):
        return self.players[self.current_player]

    def get_table_by_level(self, level) -> typing.List[SplendorCard]:
        """Map integer level to tables"""
        if level == 0:
            return self.table_low
        elif level == 1:
            return self.table_mid
        elif level == 2:
            return self.table_high
        else:
            raise ValueError(f"Invalid level {level}")

    def get_deck_by_level(self, level) -> SplendorDeck:
        """Map integer level to decks"""
        if level == 0:
            return self.deck_low
        elif level == 1:
            return self.deck_mid
        elif level == 2:
            return self.deck_high
        else:
            raise ValueError(f"Invalid level {level}")

    def game_over(self):
        for i, player in enumerate(self.players):
            if player.points >= 15:
                print(f"Player {i} has won!")
                return True
        else:
            return False
