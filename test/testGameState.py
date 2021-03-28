import unittest
import sys
sys.path.append('../src')
from NineXOGameState import NineXOGameState

class TestGameState(unittest.TestCase):
    def setUp(self):
        self.state = NineXOGameState()

    def testInit(self):
        resultStateDict = {
        "boards": [['' for i in range(9)] for i in range(9)], 
        "wonBoards": ['' for i in range(9)], 
        "lastPlayed": -1, 
        "turn": 'X'
        }

        self.assertEquals(self.state.getStateDict(), resultStateDict)

    def testMakeMove(self):
        resultStateDict = {
        "boards": [['' for i in range(9)] for i in range(9)], 
        "wonBoards": ['' for i in range(9)], 
        "lastPlayed": -1, 
        "turn": 'X'
        }

        resultStateDict["boards"][2][2] = 'X'
        resultStateDict["lastPlayed"] = 2

        self.state.makeMove(2, 2)

        self.assertEquals(resultStateDict, self.state.getStateDict())

    def testTurn(self):
        resultStateDict = {
        "boards": [['' for i in range(9)] for i in range(9)], 
        "wonBoards": ['' for i in range(9)], 
        "lastPlayed": -1, 
        "turn": 'O'
        }

        self.state.togglePlayer()

        self.assertEquals(resultStateDict, self.state.getStateDict())

    def testValidMoveHappyPath(self):
        self.state.lastPlayed = 1
        self.assertEquals(True, self.state.checkIfMoveValid(1,2))

    def testValidMoveWrongLastPlayer(self):
        self.state.lastPlayed = 3
        self.assertEquals(False, self.state.checkIfMoveValid(1,2))
        
    def testValidMoveBoardIsWon(self):
        self.state.wonBoards[1] = 'X'
        self.assertEquals(False, self.state.checkIfMoveValid(1,2))

    def testValidMoveSpaceTaken(self):
        self.state.boards[1][2] = 'X'
        self.assertEquals(False, self.state.checkIfMoveValid(1,2))

    def testValidMoveGameOver(self):
        self.state.wonBoards[0] = 'X'
        self.state.wonBoards[1] = 'X'
        self.state.wonBoards[2] = 'X'
        self.assertEquals(False, self.state.checkIfMoveValid(4,2))

    def testCheckWinNoMoves(self):
        board = ['','','','','','','','','']
        self.assertEquals(self.state.boardWin(board), '')
    
    def testCheckWinHorizontal(self):
        board = ['X','X','X','','','','','','']
        self.assertEquals(self.state.boardWin(board), 'X')

    def testCheckWinVertical(self):
        board = ['O','','','O','','','O','','']
        self.assertEquals(self.state.boardWin(board), 'O')

    def testCheckWinDiagnol(self):
        board = ['','','O','','O','','O','','']
        self.assertEquals(self.state.boardWin(board), 'O')

    def testCheckWinDraw(self):
        board = ['X','X','O',
        'O','O','X',
        'X','O','X']
        self.assertEquals(self.state.boardWin(board), '~')