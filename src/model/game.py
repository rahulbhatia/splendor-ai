# Model for the Game's State Machine
#
#

from model.player import SplendorPlayer
from model.money import SplendorBank
from model.cards import SplendorDeck

class SplendorGame():
    """
    This object represents the state of the game
    """
    def __init__(self, players=4):
        self.bank = SplendorBank()
        self.deck_low = SplendorDeck(level="low")
        self.deck_mid = SplendorDeck(level="mid")
        self.deck_high = SplendorDeck(level="high")
        self.players = [SplendorPlayer(player) for player in range(players)]

    def __repr__(self):
        summary = "SPLENDOR GAME SUMMARY\n\n" \
            f"Low: {self.deck_low}\n" \
            f"Mid: {self.deck_mid}\n" \
            f"High: {self.deck_high}\n\n" \
            f"Bank    : {self.bank}\n\n"
        for i, player in enumerate(self.players):
            summary += f"{player}\n"

        return summary
