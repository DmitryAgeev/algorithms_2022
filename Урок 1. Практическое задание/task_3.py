"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

company_data = {'company_name_1': 250000,
                'company_name_2': 1337000,
                'company_name_3': 111000,
                'company_name_4': 9000,
                'company_name_5': 1234,
                }


# Вариант 1. Сложность: O(n**2)
def sorted_1(company_d: list):
    for i in range(len(company_d)):
        lowest_value_index = i
        for j in range(i +1, len(company_d)):
            if company_d[j][1] > company_d[lowest_value_index][1]:
                lowest_value_index = j
        company_d[i], company_d[lowest_value_index] = company_d[lowest_value_index], company_d[i]
    return company_d[0:3]


list_from_directory = list(company_data.items())
for i in sorted_1(list_from_directory):
    print(i[0], ':', i[1])

print('#' * 18)

# Вариант 2. Cложность: O(n log n)
max_comp = sorted(company_data.items(), key=lambda para: para[1], reverse=True)[:3]   # O(n log n)
for company in max_comp:                                                              # O(n)
    print(f'{company[0]} : {company[1]}')

print('#' * 18)

# Вариант 3. Cложность: O(n)
top_company = {}                                                                           # O(1)
temp_dict = dict(company_data)                                                             # O(1)
for i in range(3):                                                                         # O(1)
    top = max(temp_dict.items(), key=lambda val: val[1])                                   # O(n)
    top_company[top[0]] = top[1]                                                           # O(1)
    del temp_dict[top[0]]                                                                  # O(1)
for company, profit in top_company.items():                                                # O(n)
    print(f'{company} : {profit}')

# Третий вариант оптимальнее, т.к. сложность линейная и соответственно с ростом данным,
# время выполнения будет меньше, чем у линейно-логарифмической модели.
