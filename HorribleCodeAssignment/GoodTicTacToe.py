class Player():
    '''
    The Player class keeps track of individual player information.
    '''

    # Initializing the player object with a name and a symbol
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # Returns a string for the player object name
    def getName(self) -> str: 
        return self.name
    
    # Returns a string for the player object symbol
    def getSymbol(self) -> str:
        return self.symbol

class TicTacToe:
    '''
    Tracks information and runs the game.
    '''

    # Boolean that tracks if the game has been won by a player
    isGameWon = False

    # Matrix that keeps track of the board and holds individual player 
    boardState = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]

    # Matrix that shows each squares X, Y
    boardKey = [
        ["0,0", "0,1", "0,2"],
        ["1,0", "1,1", "1,2"],
        ["2,0", "2,1", "2,2"]
    ]

    # Initializatino of the TicTacToe object. 
    # Creates 2 player objects and prints empty board. 
    def __init__(self, p1, p2):
        self.player1 = Player(p1, "X")
        self.player2 = Player(p2, "Y")
        self.printBoard()

    # Places a players symbol on a given spot on the board.
    # Returns True if input is invalid
    def placeSymbol(self, input, X, Y) -> bool:
        if self.boardState[X][Y] == '-':
            self.boardState[X][Y] = input
            return False
        else: 
            print("space is already covered by a player's input!")
            return True

    # Checks game state for winning positions. 
    def checkGameState(self, input) -> bool:
        self.isGameWon = (
            any(all(self.boardState[row][col] == input for col in range(3)) for row in range(3)) or
            any(all(self.boardState[row][col] == input for row in range(3)) for col in range(3)) or
            all(self.boardState[i][i] == input for i in range(3)) or
            all(self.boardState[i][2 - i] == input for i in range(3))
        )
        return self.isGameWon

    # Prints the board state for the current game
    def printBoard(self):
        for row in self.boardState:
            for element in row:
                print(element, end=' ')
            print()
        print()

    # Checks inputs for X and Y, checking if they are valid
    def checkInputs(self, X, Y):
        if 0 <= X <= 2 and 0 <= Y <= 2:
            return False
        print("Out of bounds! Please try again")
        return True

    # Runs the turn for a designated player 
    # Takes inputs, palces them on the board and checks the game state
    # Returns True if palceSymbol Fails
    def turn(self, player) -> bool:
        print("Player", player.getName(), "please input your desired location: ")
        X = int(input("Which Row? (0, 1, or 2) "))
        Y = int(input("Which Column? (0, 1, or 2) "))
        if self.checkInputs(X, Y) or self.placeSymbol(player.getSymbol(), X, Y):
            return True
        self.printBoard()
        if self.checkGameState(player.getSymbol()):
            print(player.getName(), "has won!")
        return False

    # Runs the game until compleation
    # turnSqeuence switches turns between the two players
    # change turn sequence if there is no failure during the turn
    def run(self):
        turnSequence = True
        print()
        while not self.isGameWon:
            if turnSequence:
                failure = self.turn(self.player1)
            else:
                failure =  self.turn(self.player2)
            if not failure: turnSequence = not turnSequence



game = TicTacToe("N", "K")
game.run()