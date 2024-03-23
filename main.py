# Initial boardstate:
rows, cols = (3, 3)
squares_array = [[" " for i in range(cols)] for j in range(rows)]

inital_board = \
"#############\n\
# {} # {} # {} #\n\
#############\n\
# {} # {} # {} #\n\
#############\n\
# {} # {} # {} #\n\
#############".format(squares_array[0][0],squares_array[0][1],squares_array[0][2],
                      squares_array[1][0],squares_array[1][1],squares_array[1][2],
                      squares_array[2][0],squares_array[2][1],squares_array[2][2])

print(inital_board)
