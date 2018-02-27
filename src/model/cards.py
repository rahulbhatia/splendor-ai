import pandas as pd

from collections import namedtuple
from random import shuffle


CARDS = "src/static/cards.csv"
LEVEL_MAP = {"low": "I", "mid": "II", "high": "III"}
CARDS_DF = pd.read_csv(CARDS).fillna(value=0)

class SplendorDeck():
    """
    This object manages the state of a deck
    """
    def __init__(self, level):
        self.level = level
        cards = CARDS_DF[CARDS_DF.Level == LEVEL_MAP[level]]
        self.cards = []
        for i, row in cards.iterrows():
            self.cards.append(
                SplendorCard(
                    level= row.Level,
                    cost=SplendorCost(
                        red=int(row.Red),
                        green=int(row.Green),
                        blue=int(row.Blue),
                        white=int(row.White),
                        black=int(row.Black)
                    ),
                    value=int(row.Value),
                    color=row.Color
                )
            )
        shuffle(self.cards)


    def __repr__(self):
        return f"{self.level:4} Deck | Count: {len(self)}"

    def __len__(self):
        return len(self.cards)

    def draw(self):
        return self.cards.pop()

class SplendorCard():
    """
    Defines a Card
    """
    def __init__(self, level, cost, value, color):
        self.level = level
        self.cost = cost
        self.value = value
        self.color = color

    def __repr__(self):
        return f"{self.color}(Value={self.value},{self.cost})"

class SplendorCost():
    def __init__(self, red, green, blue, white, black):
        self.cost = {
            "red": red,
            "green": green,
            "blue": blue,
            "white": white,
            "black": black
        }
        self.red = red
        self.blue = blue
        self.green = green
        self.white = white
        self.black = black

    def __repr__(self):
        string = "Cost("
        string += ",".join(
            [f"{color}={self.cost[color]}" for color in self.cost.keys()
                if self.cost[color] > 0])
        string += ")"
        return string

class SplendorMove():
    """
    This object stores all types of moves that can be explored at any given point
    """
    pass
