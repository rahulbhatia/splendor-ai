"""

"""

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

