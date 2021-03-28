from NineXOGameMeta import NineXOGameMeta
from GameManager import GameManager

class NineXOGameManager(GameManager):
    def createGameMeta(self):
        return NineXOGameMeta()