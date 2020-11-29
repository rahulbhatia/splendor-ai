"""
Model a player and their state
"""
import typing
from copy import deepcopy
from model.cards import SplendorCard, SplendorCost

from model.money import SplendorBank


class SplendorPlayer():
    """
    This object encompasses a player's state
    """
    def __init__(self, number):
        self.number = number
        self.bank = SplendorBank(initial=0)
        self.cards : typing.Set[SplendorCard] = set()

    def __repr__(self):
        return f"Player {self.number} | Score {self.points} | Bank {str(self.bank)} /\\ {len(self.cards)}"

    @property
    def points(self):
        points = 0
        for card in self.cards:
            points += card.value
        return points

    @property
    def wallet(self):
        buying_power = deepcopy(self.bank)
        for card in self.cards:
            buying_power.stacks[card.color.upper()].count += 1
        return buying_power.stacks

    def deduct(self, cost: SplendorCost) -> SplendorCost:
        coin_cost = {}
        for color, cost in cost.cost.items():
            coin_cost[color] = cost - self._card_buying_power(color)
            self.bank.stacks[color.upper()].count -= coin_cost[color]
        return SplendorCost(**coin_cost)

    def _card_buying_power(self, color):
        count = 0
        for card in self.cards:
            if card.color == color:
                count += 1
        return count
