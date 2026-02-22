class TicTacToe:

    done = False

    matrix = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]

    matix2 = [
        ["00", "01", "02"],
        ["10", "11", "12"],
        ["20", "21", "22"]
    ]

    def __init__(self):
        pass

    def move(self, input, X, Y):
        if not self.done:
            self.matrix[X][Y] = input
        if self.matrix[0][0] == input and self.matrix[0][1] == input and self.matrix[0][2] == input:
            self.done = True
        if self.matrix[0][0] == input and self.matrix[1][0] == input and self.matrix[2][0] == input:
            self.done = True
        if self.matrix[0][0] == input and self.matrix[1][1] == input and self.matrix[2][2] == input:
            self.done = True
        if self.matrix[0][2] == input and self.matrix[1][1] == input and self.matrix[2][0] == input:
            self.done = True
        if self.matrix[0][2] == input and self.matrix[1][2] == input and self.matrix[2][2] == input:
            self.done = True
        if self.matrix[0][1] == input and self.matrix[1][1] == input and self.matrix[2][1] == input:
            self.done = True
        if self.matrix[1][0] == input and self.matrix[1][1] == input and self.matrix[1][2] == input:
            self.done = True
        if self.matrix[2][0] == input and self.matrix[2][1] == input and self.matrix[2][2] == input:
            self.done = True
        return self.done

    def printBoard(self):
        for row in self.matrix:
            for element in row:
                print(element, end=' ')
            print() # prints a new line after each row
        print()

    def run(self):
        player1 = input("Name of Player 1: ")
        player2 = input("Name of Player 2: ")
        player1Turn = True
        self.printBoard()
        print()
        while not self.done:
            if player1Turn:
                print("New turn!", player1, "please input your desired location: ")
                X = int(input("Which Row? (0, 1, or 2)"))
                Y = int(input("Which Column? (0, 1, or 2)"))
                self.move("X", X, Y)
            else:
                print("New turn!", player2, "please input your desired location: ")
                X = int(input("Which Row? (0, 1, or 2)"))
                Y = int(input("Which Column? (0, 1, or 2)"))
                self.move("Y", X, Y)
            self.printBoard()
            player1Turn = not player1Turn



game = TicTacToe()
game.run()