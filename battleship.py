from random import random, randint
hit_board = []
enemy_ship_board = []

for x in range(10):
    hit_board.append(["0"] * 10)
    enemy_ship_board.append(["0"] * 10)

def new_screen():
    print("Battleship!")
    print_board(hit_board)

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def random_position(board, xBound, yBound):
    xCoordinate = randint(0, (len(board) - 1) - xBound)
    yCoordinate = randint(0, (len(board[0]) - 1) - yBound)
    return (xCoordinate, yCoordinate)

class Ship:
    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.direction = (int)(random() * 2) * 90
        self.positions = []
        self.damage = 0

        empty_space = False
        row = 0
        col = 0

        while not empty_space:
            empty_space = True
            if self.direction == 0:
                (row, col) = random_position(hit_board, self.size, 0)
                for i in range(self.size):
                    if enemy_ship_board[row + i][col] == 1:
                        empty_space = False
                        break
            elif self.direction == 90:
                (row, col) = random_position(hit_board, 0, self.size)
                for i in range(self.size):
                    if enemy_ship_board[row][col + i] == 1:
                        empty_space = False
                        break
        if self.direction == 0:
            for i in range(size):
                self.positions.append([row + i, col])
                enemy_ship_board[row + i][col] = 1
        elif self.direction == 90:
            for i in range(size):
                self.positions.append([row, col + i])
                enemy_ship_board[row][col + i] = 1
        elif self.direction == 90:

ships = []
ships.append(Ship("submarine", 1))
ships.append(Ship("corsair", 2))
ships.append(Ship("cruiser", 3))
ships.append(Ship("battleship", 4))
ships.append(Ship("carrier", 5))

