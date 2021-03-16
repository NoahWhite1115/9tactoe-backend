import uuid
from GameMeta import GameMeta, NineXOGameMeta

class GameManager():
    def __init__(self, timeout):
        self.game_hash = {}
        self.game_count = 0
        self.timeout = timeout
        self.player_hash = {}

    def createGame(self):
        gid = uuid.uuid4().hex[:8].lower()
        while gid in self.game_hash:
            gid = uuid.uuid4().hex[:8].lower()

        self.game_hash[gid] = self.createGameMeta()

        self.game_count += 1
        return gid

    def get_list(self):
        print(len(self.game_hash))
        for i in self.game_hash.keys():
            print(i)

    def get_game(self, gid):
        return self.game_hash[gid]

    def createGameMeta(self):
        return GameMeta()

    def addPlayer(self, gid, sid):
        self.player_hash[sid] = gid
        game = self.game_hash[gid]
        return(game.addPlayer(sid))

    def removePlayer(self, sid):
        try: 
            gid = self.player_hash[sid]
            game = self.game_hash[gid]
            game.removePlayer(sid)
            del self.player_hash[sid]
        except(KeyError):
            return 

class NineXOGameManager(GameManager):
    def createGameMeta(self):
        return NineXOGameMeta()