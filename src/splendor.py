"""
Run the game
"""
import random
from model.action.purchase_action import PurchaseAction
from model.game import SplendorGame

MAX_TURNS = 1000

def random_agent(state, actions):
    return random.choice(actions)


def greedy_buyer(state, actions):
    purchases = list(filter(lambda action: isinstance(action, PurchaseAction), actions))
    if len(purchases) > 0:
        return random.choice(purchases)
    else:
        return random.choice(actions)


def main():
    states = [SplendorGame()]
    for i in range(MAX_TURNS):
        options = states[-1].available_moves()
        if len(options) == 0:
            print(f"{states[-1].current_player}: No Options for player!")
            break
        choice = greedy_buyer(states[-1], options)
        print(f"{states[-1].current_player}: {choice}")
        states.append(choice.transform(states[-1]))
        if states[-1].game_over():
            break
    print(states[-1])


if __name__ == "__main__":
    main()
