import abc
import typing


class SplendorAction(abc.ABC):
    def __init__(self):
        pass

    def __repr__(self):
        return self.__name__

    def transform(self, game_state):
        """
        Return a new Splendor Game with the state representing the new game
        """
        raise NotImplementedError("This is an abstract action")
    
    @abc.abstractstaticmethod
    def possibilities(game_state):
        ...