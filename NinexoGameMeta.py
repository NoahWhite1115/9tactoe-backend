from GameState import GameState
from GameMeta import GameMeta

class NineXOGameMeta(GameMeta):
    def __init__(self):
        super().__init__()
        self.players = players = {'X': None, 'O': None}

    def makeGameState(self):
        return GameState()
    
    def addPlayer(self, sid):
        if (self.players['X'] == None):
            print("It was player X!")
            self.players['X'] = sid
            return 'X'
        elif (self.players['O'] == None):
            print("It was player O!")
            self.players['O'] = sid
            return 'O'
        else:
            self.spectators.append(sid)
            return 'Spec'

    def removePlayer(self, sid):
        if (self.players['X'] == sid):
            self.players['X'] = None

        elif (self.players['O'] == sid):
            self.players['O'] = None

        #TODO: error proof this 
        else:
            self.spectators.remove(sid)

    def checkPlayer(self, sid):
        if (self.players[self.gameState.turn] != sid):
            print("Wrong player clicked!")
            return False

        if self.players['X'] == None or self.players['O'] == None:
            print("Not enough players connected!")
            return False

        return True

    def handleClick(self, sid, clickData):
        if self.gameMeta.checkPlayer(sid):
            i = clickData['i']
            j = clickData['j']
            
            if self.gameState.checkIfMoveValid(i,j):
                self.gameState.makeMove(i,j)
                self.gameState.togglePlayer()

        return self.getStateDict()