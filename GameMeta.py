from abc import ABC, abstractmethod
from datetime import utcnow

class GameMeta(ABC):
    def __init__(self):
        self.gameState = self.makeGameState()
        self.players = {}
        self.spectators = []
        self.gameWon = False
        self.timestamp = utcnow()

    def getStateDict(self):
        return self.gameState.getStateDict()

    """
    makeGame: makes a new game state object
    takes: 
    returns: a new game state object
    """
    @abstractmethod
    def makeGameState(self):
        return NotImplemented

    """
    addPlayer: adds a player to the game
    takes: a player socket id
    returns: the role assigned to the player, as a string
    """
    @abstractmethod
    def addPlayer(self, sid):
        return NotImplemented

    """
    removePlayer: removes a player from the game
    takes: a player socket id
    returns: boolean indicating if the player was removed
    """
    @abstractmethod
    def removePlayer(self, sid):
        return NotImplemented

    """
    handleClick: adds a player to the game
    takes:
        sid, a player socket id
        clickObject, a data structure containing data relevant to the click event
    returns: the state of the game after the click is handled
    """
    @abstractmethod
    def handleClick(self, sid, clickObject):
        return NotImplemented

    """
    gameReady: returns true when all players have joined
    takes: 
    returns: true if the game is ready to start, false otherwise
    """
    @abstractmethod
    def gameReady(self):
        return NotImplemented

def updateTime(function):
    def updateTimeInternal(self):
        self.timestamp = utcnow()
        function(self)