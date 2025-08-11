# Exercise 7:
# Choose a suitable type for storing a chess board state
# and write a sample data structure with 2 rows

chess_board = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'], 
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP']  
]


for row in chess_board:
    for row1 in row:
        print(row1)