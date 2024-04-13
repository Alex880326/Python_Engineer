# -*- coding: utf-8 -*-
"""HomePython_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cy7oJx9NatsO4b3xW08qdUcd6wsk2Yb2

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

def type_of_triangle(a, b, c):
    if a == b and b == c:
        return "Равносторонний"
    elif a == b or a == c or b == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if is_triangle(a, b, c):
      print("Тип треугольника: " + type_of_triangle(a, b, c))
else:
      print("Треугольника с такими сторонами не существует.")

"""Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

def check_prime(n):
    if n <= 1 or n > 100000:
        return "Больше 100 тысяч"

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "Составное"

    return "Простое"

num = int(input("Введите число: "))

result = check_prime(num)
print(f"Число {num}  {result}.")

"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

print("Программа загадала число от 0 до 1000. Угадайте его за 10 попыток.")

for attempt in range(attempts):
    guess = int(input(f"Попытка {attempt+1}. Введите ваше предположение: "))

    if guess < num_to_guess:
        print("Больше")
    elif guess > num_to_guess:
        print("Меньше")
    else:
        print(f"Поздравляю, вы угадали число {num_to_guess}!")
        break

if guess != num_to_guess:
    print(f"Вы проиграли. Загаданное число было: {num_to_guess}")