def is_game_over(squares_array):
    for row in squares_array:
        if row[0] == 'X' or row[0] == 'O':
            if len(set(row)) == 1:
                return True
    return False
# Initial boardstate:
rows, cols = (3, 3)
squares_array = [[" " for i in range(cols)] for j in range(rows)]

def alternate_between_x_and_o():
    while True:
        yield "O"
        yield "X"

def display_board(squares_array):
    inital_board = \
    "      #############\n\
    0 # {} # {} # {} #\n\
      #############\n\
    1 # {} # {} # {} #\n\
      #############\n\
    2 # {} # {} # {} #\n\
    y #############\n\
      x 0   1   2".format(squares_array[0][0],squares_array[0][1],squares_array[0][2],
                          squares_array[1][0],squares_array[1][1],squares_array[1][2],
                          squares_array[2][0],squares_array[2][1],squares_array[2][2])

    print(inital_board)

display_board(squares_array)

# Game Loop
input_x = 0
input_y = 0

game_over = False
placement_character = "X"
alternator = alternate_between_x_and_o()
while (input_x != -1 and input_y != -1) or game_over == True:

    input_x = int(input("Input x value: "))
    input_y = int(input("Input y value: "))

    if (squares_array[input_y][input_x] == " "):
        squares_array[input_y][input_x] = placement_character
        game_over = is_game_over(squares_array)
        display_board(squares_array)
        placement_character = next(alternator)
    else:
        print("Please retry input")