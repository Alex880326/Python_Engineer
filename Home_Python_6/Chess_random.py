# Ex 3
# Шахматный модуль с генерацией случайной расстановки Ферзей

import random

def generate_board():
    return [random.randint(0, 7) for _ in range(8)]

def check_queens(board):
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return False
    return True


