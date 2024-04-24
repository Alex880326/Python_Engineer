# Ex 3.1 
# Генерация сучаной расстановки
from Chess_random import generate_board
from Battle_exodus import check_queens

queens_positions = generate_board() # Случайная расстановка

# queens_positions = (2, 5, 1, 4, 7, 0, 6, 3) Дружная позиция
# queens_positions = (3, 5, 2, 7, 3, 4, 7, 5) Враждебная позиция

if __name__ == '__main__':
    if check_queens(queens_positions):
        print("Ферзи не бьют друг друга.")
    else:
        print("Есть ферзи, которые бьют друг друга.")

