from random import randrange

game_over = False
board_array = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
grid_positions = {
    "1": (0,0),
    "2": (0,1),
    "3": (0,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "7": (2,0),
    "8": (2,1),
    "9": (2,2),
}


#Create initial board and update with every turn
def display_board():
    game_board = "+-------+-------+-------+\n"
    for row in board_array:
        game_board += "|       |       |       |\n"
        for item in row:
            game_board += f"|   {item}   "
        game_board += "|\n|       |       |       |\n"
        game_board += "+-------+-------+-------+\n"

    return print(game_board)


#Players move
def enter_move():
    if not game_over:
        user_position = input("Enter your move: ")
        try:
            position = grid_positions[user_position]
            free_positions = make_list_of_free_fields()
            if position not in free_positions:
                print("Already taken")
                enter_move()
            row,col = position[0], position[1]
            board_array[row][col] = "O"
            check_win("O")
            return display_board()
        except KeyError:
            print("Invalid input")
            enter_move()
            

#Function to make a list of the free grid positions   
def make_list_of_free_fields(): 
    free_space = []
    for i in range(len(board_array)):
        for j in range(len(board_array[i])):
            if board_array[i][j] == "X" or board_array[i][j] == "O":
                pass
            else:
                free_space.append((i,j))
    return free_space

    
def draw_move():
    #Draw a random move from the computer
    if not game_over:
        free_spaces = make_list_of_free_fields()
        print(free_spaces)
        computer_pos = randrange(0,len(free_spaces))
        position = free_spaces[computer_pos]
        row,col = position[0], position[1]
        board_array[row][col] = "X"
        check_win("X")
        return display_board()
    

def check_win(symbol):
    #Check Horizontal
    global game_over
    for i in board_array:
        if i[0] == symbol and i[1] == symbol and i[2] == symbol:
            game_over = True
            return print(f"{symbol} wins!")
            
            
    #Check Vertical
    if board_array[0][0] == symbol and board_array[1][0] == symbol and board_array[2][0] == symbol:
        game_over = True
        return print(f"{symbol} wins!")
    
    elif board_array[0][1] == symbol and board_array[1][1] == symbol and board_array[2][1] == symbol:
        game_over = True
        return print(f"{symbol} wins!")
    
    elif board_array[0][2] == symbol and board_array[1][2] == symbol and board_array[2][2] == symbol:
        game_over = True
        return print(f"{symbol} wins!")
    
    
    #Check Horizontal
    if board_array[0][0] == symbol and board_array[1][1] == symbol and board_array[2][2] == symbol:
        game_over = True
        return print(f"{symbol} wins!")
    
    elif board_array[0][2] == symbol and board_array[1][1] == symbol and board_array[2][0] == symbol:
        game_over = True
        return print(f"{symbol} wins!")
    

display_board()

#Main Game loop
while len(make_list_of_free_fields()) != 0 and not game_over: 
    enter_move()
    make_list_of_free_fields()
    draw_move()

