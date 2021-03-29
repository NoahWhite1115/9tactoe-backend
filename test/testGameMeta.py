import unittest
import sys
from unittest.mock import Mock
sys.path.append('../src')
from NineXOGameMeta import NineXOGameMeta

class TestGameState(unittest.TestCase):
    def setUp(self):
        self.meta = NineXOGameMeta()
        self.meta.gameState = Mock()

    def testAddPlayers(self):
        self.assertEqual('X', self.meta.addPlayer("1234567"))
        self.assertEqual('O', self.meta.addPlayer("1234568"))
        self.assertEqual('Spectator', self.meta.addPlayer("1234569"))
        self.assertEqual({'X': "1234567", 'O': "1234568"}, self.meta.players)

    def testGameReady(self):
        self.assertEqual('X', self.meta.addPlayer("1234567"))
        self.assertEqual('O', self.meta.addPlayer("1234568"))
        self.assertEqual(True, self.meta.gameReady())

    def testRemoveHappyPath(self):
        self.assertEqual('X', self.meta.addPlayer("1234567"))
        self.assertEqual(True, self.meta.removePlayer("1234567"))
        self.assertEqual({'X': None, 'O': None}, self.meta.players)

    def testRemoveFailure(self):
        self.assertEqual('X', self.meta.addPlayer("1234567"))
        self.assertEqual(False, self.meta.removePlayer("1234568"))
        self.assertEqual({'X': "1234567", 'O': None}, self.meta.players)

    def testCheckPlayerHappyPath(self):
        self.meta.gameState.turn = 'X'

        self.assertEqual('X', self.meta.addPlayer("1234567"))
        self.assertEqual('O', self.meta.addPlayer("1234568"))

        self.assertEqual(True, self.meta.checkPlayer("1234567"))

    def testCheckPlayerWrongTurn(self):
        self.meta.gameState.turn = 'O'

        self.assertEqual('X', self.meta.addPlayer("1234567"))
        self.assertEqual('O', self.meta.addPlayer("1234568"))

        self.assertEqual(False, self.meta.checkPlayer("1234567"))

    def testCheckPlayerNotEnough(self):
        self.meta.gameState.turn = 'X'

        self.assertEqual('X', self.meta.addPlayer("1234567"))

        self.assertEqual(False, self.meta.checkPlayer("1234567"))

    def testHandleClick(self):
        self.meta.gameState.checkIfMoveValid.return_value = True
        self.meta.gameState.getStateDict.return_value = {}

        self.meta.gameState.turn = 'X'

        self.assertEqual('X', self.meta.addPlayer("1234567"))
        self.assertEqual('O', self.meta.addPlayer("1234568"))

        self.meta.handleClick("1234567", {'i':2, 'j':2})

