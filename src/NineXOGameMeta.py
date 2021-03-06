from NineXOGameState import NineXOGameState
from GameMeta import GameMeta
from datetime import datetime  

class NineXOGameMeta(GameMeta):
    def __init__(self):
        super().__init__()
        self.players = players = {'X': None, 'O': None}

    def makeGameState(self):
        return NineXOGameState()
    
    def addPlayer(self, sid):
        if (self.players['X'] == None):
            self.players['X'] = sid
            return 'X'
        elif (self.players['O'] == None):
            self.players['O'] = sid
            return 'O'
        else:
            self.spectators.append(sid)
            return 'Spectator'

    def removePlayer(self, sid):
        if (self.players['X'] == sid):
            self.players['X'] = None
            return True

        if (self.players['O'] == sid):
            self.players['O'] = None
            return True

        try:
            self.spectators.remove(sid)
            return True
        except(ValueError):
            return False

    def checkPlayer(self, sid):
        if (self.players[self.gameState.turn] != sid):
            print("Wrong player clicked!")
            return False

        if self.players['X'] == None or self.players['O'] == None:
            print("Not enough players connected!")
            return False

        return True

    def handleClick(self, sid, clickData):
        #maybe move timestamp to super?
        self.timestamp = datetime.now()
        
        if self.checkPlayer(sid):
            i = clickData['i']
            j = clickData['j']
            
            if self.gameState.checkIfMoveValid(i,j):
                self.gameState.makeMove(i,j)
                self.gameState.togglePlayer()

        return self.getStateDict()

    def gameReady(self):
        if (self.players['X'] != None and self.players['O'] != None):
            return True
        else:
            return False
