import pandas as pd
from collections import namedtuple

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
                    level = row.Level,
                    cost = SplendorCost(
                        red=row.Red,
                        green=row.Green,
                        blue=row.Blue,
                        white=row.White,
                        black=row.Black
                    ),
                    value = row.Value,
                    color = row.Color
                )
            )

    def __repr__(self):
        return "deck"

    def __len__(self):
        return len(self.cards)

class SplendorCard():
    """
    Defines a Card
    """
    def __init__(self, level, cost, value, color):
        self.level = level
        self.cost = cost
        self.value = value
        self.color = color

SplendorCost = namedtuple("SplendorCost", ["red", "green", "blue", "white", "black"])

class SplendorMove():
    """
    This object stores all types of moves that can be explored at any given point
    """
    pass
