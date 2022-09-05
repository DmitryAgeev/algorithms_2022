"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


# Линейная O(n)
def search_linear(lst: list):   # O(n)
    smallest = some_list[0]     # O(1)
    for i in some_list:         # O(n)
        if i < smallest:        # O(1)
            smallest = i        # O(1)
    return smallest             # O(1)


# Квадратичная O(n**2)
def search_square(lst: list):
    for i in some_list:         # O(n)
        stop = True             # O(1)
        for el in some_list:    # O(n)
            if i > el:          # O(1)
                stop = False    # O(1)
        if stop:                # O(1)
            return i            # O(1)


some_list = [1, 2, 3, 100, 42, 13, 228, 0, 1337, 5]
print(search_linear(some_list))
print(search_square(some_list))
