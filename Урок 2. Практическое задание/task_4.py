"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def number_sum(number):
    # if number == 0:
    #     return 0
    # else:
    #     some_sum = 1 + number_sum(number - 1) / - 2
    #     return some_sum
    return 0 if number == 0 else 1 + number_sum(number - 1) / 2


num_of_number = int(input('Enter the number of elements: '))
print(f'Amount of elements: {num_of_number}, their sum: {number_sum(num_of_number)}')
