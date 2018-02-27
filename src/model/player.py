"""
Model a player and their state
"""

from model.money import SplendorBank


class SplendorPlayer():
    """
    This object encompasses a player's state
    """
    def __init__(self, number):
        self.number = number
        self.bank = SplendorBank(initial=0)
        self.cards = set()

    @property
    def wallet(self):
        buying_power = self.bank
        for card in self.cards:
            buying_power.stacks[card.color] += 1
        return buying_power.stacks

    def __repr__(self):
        return f"Player {self.number}: " + str(self.bank)
