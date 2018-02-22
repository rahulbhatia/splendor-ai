
from model.cards import SplendorDeck
from unittest import TestCase

class TestSplendorDeck(TestCase):
    """
    Test the Deck object
    """
    def test_create_deck(self):
        deck = SplendorDeck(level="low")

    def test_deck_card_count(self):
        deck = SplendorDeck(level="low")
        self.assertEquals(len(deck), 40)

        deck = SplendorDeck(level="mid")
        self.assertEquals(len(deck), 29)

        deck = SplendorDeck(level="high")
        self.assertEquals(len(deck), 20)
