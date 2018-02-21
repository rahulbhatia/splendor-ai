# Model for the Game's State Machine
# 
# 

class SplendorGame():
    """
    This object represents the state of the game
    """
    def __init__(self, players=4):
        self.bank = SplendorBank()
        self.deck_low = SplendorDeck()
        self.deck_mid = SplendorDeck()
        self.deck_high = SplendorDeck()
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
        
    
    def options(self):
        """
        Return all options
        """
        pass
    
class SplendorBank():
    """
    This object manages the state of the bank
    """
    COLORS = ["RED", "GREEN", "BLUE", "BLACK", "WHITE"]
    def __init__(self, initial=7):
        self.stacks = {}
        for color in self.COLORS:
            self.stacks[color] = SplendorStack(color, count=initial)
    
    def __repr__(self):
        return " | ".join([str(stack) for stack in self.stacks.values()]) 

class SplendorStack():
    """
    """
    def __init__(self, color, count = 0):
        self.color = color
        self.count = count
    
    def __repr__(self):
        return f"{self.color}: {self.count}"

class SplendorDeck():
    """
    This object manages the state of a deck
    """
    def __repr__(self):
        return "deck"

class SplendorPlayer():
    """
    This object encompasses a player's state
    """
    def __init__(self, number):
        self.number = number
        self.bank = SplendorBank(initial=0)
    
    def __repr__(self):
        return f"Player {self.number}: " + str(self.bank)

class SplendorMove():
    """
    This object stores all types of moves that can be explored at any given point
    """
    pass