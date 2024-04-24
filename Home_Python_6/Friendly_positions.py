# Ex 4 
# Дружественные позиции
from Chess_random import generate_board
from Chess_random import check_queens


friendly_positions = 0

while friendly_positions < 4:
    queens_board = generate_board()
    if check_queens(queens_board):
        print(f"Дружественные позиции: {queens_board}")
        friendly_positions += 1

