#Creates the board and prints it
board = []
for x in range(3):
    board.append(["|"] * 3)
def print_board(board):
    for row in board:
        print " ".join(row)
    
#Lets each player make their turn and print it on the board (if no errors happen)
def game():
    playerOneWin = "Player 1 WINS!!!"
    playerTwoWin = "Player 2 WINS!!!"
    for each in range(5):
        #Player One's turn
        print "It's player ONE's turn! X"
        
        #Makes sure there are no error in the user's response to the row        
        guess_row = raw_input("Guess Row: ")
        while guess_row == "":  #Sees if the user didn't type anything
            print "Please don't enter nothing. Please try again."
            guess_row = raw_input("Guess Row: ")
            if guess_row != "":
                break
        while True:
            if not guess_row.isdigit(): #Sees if the user types something that isn't an integer
                print "Please enter only numbers. Please try again."
                guess_row = raw_input("Guess Row: ")
            else:
                guess_row = int(guess_row)
                break

        #Makes sure there are no error in the user's response to the row        
        guess_col = raw_input("Guess Col: ")
        while guess_col == "":  #Sees if the user didn't type anything
            print "Please don't enter nothing. Please try again."
            guess_col = raw_input("Guess Col: ")
            if guess_col != "":
                break
        while True:
            if not guess_col.isdigit(): #Sees if the user types something that isn't an integer
                print "Please enter only numbers. Please try again."
                guess_col = raw_input("Guess Col: ")
            else:
                guess_col = int(guess_col)
                break
            
        
        #Sees if the numbers are between 1 and 3
        while (guess_row < 1 or guess_row > 3) or (guess_col < 1 or guess_col > 3):
            print "\nPlease choose numbers between 1 and 3. Please try again.\n"
            guess_row = int(raw_input("Guess Row: "))
            guess_col = int(raw_input("Guess Col: "))
            print '\n'
            if (guess_row == 1 or guess_row == 2 or guess_row == 3) and (guess_col == 1 or guess_col == 2 or guess_col == 3):
                break
        #Sees if a space has already been taken by the other player  
        while board[guess_row - 1][guess_col - 1] == 'O':
            print 'That space is already occupied! Please try again.\n'
            guess_row = int(raw_input("Guess Row: "))
            guess_col = int(raw_input("Guess Col: "))
            print_board(board)
            print '\n'
            if board[guess_row - 1][guess_col - 1] != 'O':
                break
        #If no errors, the space gets filled    
        board[guess_row - 1][guess_col - 1] = "X"
        print_board(board)
        print '\n'
        if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':    #Top row
            print playerOneWin
            break
        if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':    #Middle row
            print playerOneWin
            break
        if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':    #Bottom row
            print playerOneWin
            break
        if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':    #Left column
            print playerOneWin
            break
        if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':    #Middle column
            print playerOneWin
            break
        if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':    #Right column
            print playerOneWin
            break
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':    #Left diagonal
            print playerOneWin
            break
        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':    #Right diagonal
            print playerOneWin
            break

        #If the board is filled and there is no winner, this will break the loop
        if each == 4:
            print "Nobody won :("
            break
        
        #Player Two's turn
        print "It's player TWO's turn! O"
        #Makes sure there are no error in the user's response to the row        
        guess_row = raw_input("Guess Row: ")
        while guess_row == "":
            print "Please don't enter nothing. Please try again."
            guess_row = raw_input("Guess Row: ")
            if guess_row != "":
                break
        while True:
            if not guess_row.isdigit():
                print "Please enter only numbers. Please try again."
                guess_row = raw_input("Guess Row: ")
            else:
                guess_row = int(guess_row)
                break

        #Makes sure there are no error in the user's response to the row        
        guess_col = raw_input("Guess Col: ")
        while guess_col == "":
            print "Please don't enter nothing. Please try again."
            guess_col = raw_input("Guess Col: ")
            if guess_col != "":
                break
        while True:
            if not guess_col.isdigit():
                print "Please enter only numbers. Please try again."
                guess_col = raw_input("Guess Col: ")
            else:
                guess_col = int(guess_col)
                break
            
        #Sees if the numbers are between 1 and 3
        while (guess_row < 1 or guess_row > 3) or (guess_col < 1 or guess_col > 3):
            print "\nPlease choose numbers between 0 and 2. Please try again.\n"
            guess_row = int(raw_input("Guess Row: "))
            guess_col = int(raw_input("Guess Col: "))
            print '\n'
            if (guess_row == 1 or guess_row == 2 or guess_row == 3) and (guess_col == 1 or guess_col == 2 or guess_col == 3):
                break
        #Sees if a space has already been taken by the other player 
        while board[guess_row - 1][guess_col - 1] == 'X':
            print 'That space is already occupied! Please try again.\n'
            guess_row = int(raw_input("Guess Row: "))
            guess_col = int(raw_input("Guess Col: "))
            print_board(board)
            print '\n'
            if board[guess_row - 1][guess_col - 1] != 'X':
                break
        #If no errors, the space gets filled        
        board[guess_row - 1][guess_col - 1] = "O"
        print_board(board)
        print '\n'
        if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
            print playerTwoWin
            break
        if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
            print playerTwoWin
            break
        if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
            print playerTwoWin
            break
        if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
            print playerTwoWin
            break
        if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
            print playerTwoWin
            break
        if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
            print playerTwoWin
            break
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            print playerTwoWin
            break
        if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            print playerTwoWin
            break

#Starts the game
def main():
    print "Let's play Tic Tac Toe!"
    print "PLAYER 1 WILL BE: X"
    print "PLAYER 2 WILL BE: O\n"
    print "To play this game, enter the number row and number column you wish to put your letter in.\nFor example, if you want the top left square, enter 1 for both the row and the column to put your letter there.\n"
    print_board(board)
    print '\n'
    game()

main()
