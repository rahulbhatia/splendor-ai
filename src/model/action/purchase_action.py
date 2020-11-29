
from copy import deepcopy
from model.cards import LEVEL_MAP

from model.money import SplendorBank
from .splendor_action import SplendorAction


class PurchaseAction(SplendorAction):
    def __init__(self, card, level, index):
        self.card = card
        self.card_level = level
        self.card_index = index
    
    def __repr__(self):
        return(f"PurchaseAction( {self.card} )")

    def transform(self, game_state):
        # TODO Something is wrong with this transition! It looks like user's can go into negative coin ownership
        new_state = deepcopy(game_state)
        current_player = new_state.get_current_player()
        current_player.cards.add(self.card)
        coin_cost = current_player.deduct(self.card.cost)
        new_state.bank.increment(coin_cost)
        deck = new_state.get_deck_by_level(self.card_level)
        new_state.get_table_by_level(self.card_level)[self.card_index] = deck.draw()
        new_state.current_player = (game_state.current_player + 1) % len(game_state.players)
        return new_state

    @staticmethod
    def possibilities(game_state):
        actions = []
        current_buying_power = game_state.players[game_state.current_player].wallet
        for r, table_row in enumerate([game_state.table_high, game_state.table_mid, game_state.table_low]):
            for i, card in enumerate(table_row):
                if (card is not None) & PurchaseAction._can_purchase(current_buying_power, card):
                    actions.append(PurchaseAction(card, r, i)) 
        return actions

    @staticmethod
    def _can_purchase(stacks: dict, card):
        if card is None:
            return False
        for color in SplendorBank.COLORS:
            if card.cost.cost[color.lower()] > stacks[color].count:
                return False
        return True
