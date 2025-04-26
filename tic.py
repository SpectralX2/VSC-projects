# create the array for the board and fill it with empty spaces
board = []
for i in range(9):
    board.append(" ")
player = 1
count = 0
play_game = True

while (play_game):
    # print out the current board in the terminal
    print("  0   1   2")
    print("0 {} | {} | {} |".format(board[0], board[1], board[2]))
    print(" ------------")
    print("1 {} | {} | {} |".format(board[3], board[4], board[5]))
    print(" ------------")
    print("2 {} | {} | {} |".format(board[6], board[7], board[8]))
    # get the current players input and check that it is valid
    print("Player {}".format(player))
    row = int(input("Enter row: "))
    while (row < 0 or row > 2):
        print("Invalid input. Please try again.")
        row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    while (col < 0 or col > 2):
        print("Invalid input. Please try again.")
        col = int(input("Enter column: "))
    # and add the play to the board
    index = row * 3 + col
    while (board[index] != " "):
        print("That space is already taken.")
        row = int(input("Enter row: "))
        while (row < 0 or row > 2):
            print("Invalid input. Please try again.")
            row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        while (col < 0 or col > 2):
            print("Invalid input. Please try again.")
            col = int(input("Enter column: "))
        index = row * 3 + col
    else:
        if (player == 1):
            board[index] = "x"
        else:
            board[index] = "o"
    # check if the game is over
    if ((board[0] != " " and board[0] == board[1] and board[0] == board[2])
    or (board[3] != " " and board[3] == board[4] and board[3] == board[5])
    or (board[6] != " " and board[6] == board[7] and board[6] == board[8])
    or (board[0] != " " and board[0] == board[3] and board[0] == board[6])
    or (board[1] != " " and board[1] == board[4] and board[1] == board[7])
    or (board[2] != " " and board[2] == board[5] and board[2] == board[8])
    or (board[0] != " " and board[0] == board[4] and board[0] == board[8])
    or (board[2] != " " and board[2] == board[4] and board[2] == board[6])):
        # print out the current board in the terminal
        print(" 0     1    2")
        print("0 {} | {} | {} |".format(board[0], board[1], board[2]))
        print(" --------------")
        print("1 {} | {} | {} |".format(board[3], board[4], board[5]))
        print(" --------------")
        print("2 {} | {} | {} |".format(board[6], board[7], board[8]))
        print("Player {} wins!".format(player))
        play_game = False
    count += 1
    if count > 8:
        play_game = False
        print("Tie Game")
    # move on to the next player
    if player == 1:
        player = 2
    else:
        player = 1