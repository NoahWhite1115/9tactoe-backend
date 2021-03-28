from abc import ABC, abstractmethod

class GameState(ABC):
    def __init__(self):
        self.reset()

    """
    reset: resets the game to it's inital state
    takes: nothing
    returns: nothing
    """
    @abstractmethod
    def reset(self):
        return NotImplemented

    """
    getStateDict: returns a dictionary representing game state
    takes: nothing
    returns: a dictionary of the game state
    """
    @abstractmethod
    def getStateDict(self):
        return NotImplemented

    """
    getStateDict: returns a dictionary representing game state
    takes: nonthing
    returns: a dictionary of the game state
    """
    @abstractmethod
    def getStateDict(self):
        return NotImplemented