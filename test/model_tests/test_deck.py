
from model.cards import SplendorDeck
from unittest import TestCase

class TestSplendorDeck(TestCase):
    """
    Test the Deck object
    """
    def test_create_deck(self):
        """
        Can we instantiate a deck?
        """
        deck = SplendorDeck(level="low")

    def test_deck_card_count(self):
        """
        Do the decks start with the right amount of cards
        """
        deck = SplendorDeck(level="low")
        self.assertEquals(len(deck), 40)

        deck = SplendorDeck(level="mid")
        self.assertEquals(len(deck), 29)

        deck = SplendorDeck(level="high")
        self.assertEquals(len(deck), 20)
