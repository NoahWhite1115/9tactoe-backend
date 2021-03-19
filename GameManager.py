import uuid
from GameMeta import GameMeta

class GameManager():
    def __init__(self, timeout):
        #gid -> game map
        self.game_hash = {}
        self.game_count = 0
        self.timeout = timeout
        #sid -> gid map
        self.player_hash = {}

    """
    createGame: makes a new game meta
    takes: 
    returns: the game id as a string
    """
    def createGame(self):
        gid = uuid.uuid4().hex[:8].lower()
        while gid in self.game_hash:
            gid = uuid.uuid4().hex[:8].lower()

        self.game_hash[gid] = self.createGameMeta()

        self.game_count += 1
        return gid

    """
    getGame: gets a game with a matching id
    takes: a game id as a string 
    returns: a new game state object
    """
    def getGame(self, gid):
        return self.game_hash[gid]

    """
    createGameMeta: creates a new game meta
    overload when creating a new subclass
    """
    def createGameMeta(self):
        return GameMeta()

    """
    addPlayer: adds a player to a game
    takes:
        gid: game id as a string
        sid: socket io socket id
    returns: role of the player
    throws: GameNotAvailibleException
    """
    def addPlayer(self, gid, sid):
        self.player_hash[sid] = gid
        try:
            game = self.game_hash[gid]
        except(KeyError):
            raise GameNotAvailibleException(gid)
        return(game.addPlayer(sid))


    """
    removePlayer: removes a player from a game
    takes: player sid 
    returns: nothing
    """
    def removePlayer(self, sid):
        try: 
            gid = self.findPlayer(sid)        
            game = self.game_hash[gid]
            game.removePlayer(sid)
            del self.player_hash[sid]
        except(KeyError):
            #add logging here once it's ready
            return 

    """
    findPlayer: gets the gid of the game the player is in
    takes: sid of the player to look up
    returns: gid of the game the player is in
    throws: PlayerNotFoundException 
    """
    def findPlayer(self, sid):
        try: 
            return self.player_hash[sid]
        except(KeyError):
            raise PlayerNotFoundException


#Export these to their own file later
class GameNotAvailibleException(KeyError):
     def __init__(self, gid, message="Game with that gid does not exist"):
        self.message = message
        super().__init__(self.message)

class PlayerNotFoundException(KeyError):
    def __init__(self, sid, message="Player with that id is not in any games"):
        self.message = message
        super().__init__(self.message)
