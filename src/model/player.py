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
    
    def __repr__(self):
        return f"Player {self.number}: " + str(self.bank)