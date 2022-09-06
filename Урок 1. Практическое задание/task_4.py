"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# Вариант 1. Сложность: O(1)
def variant_1(profiles: dict, login: str, password: int):
    if profiles.get(login.lower()):
        if profiles.get(login.lower())[0] != password:
            return 'Wrong password!'
        elif profiles.get(login.lower())[0] == password and profiles.get(login.lower())[1]:
            return 'Welcome!'
        else:
            return 'Wrong user!'
    else:
        return 'Wrong login!'


# Вариант 2. Сложность: O(n)
def variant_2(profiles: dict, login: str, password: int):
    for key, val in profiles.items():
        if key == login.lower():
            if val[0] == password and val[1]:
                return 'Welcome!'
            elif val[0] != password:
                return 'Wrong password!'
            elif val[0] == password and not val[1]:
                return 'Wrong user!'
    return 'Wrong login!'


# Первый вариант оптимальнее

user_profiles = {'Max': [123, False],
                 'Leo': [777, True],
                 'Bob': [111, True]
                 }

user_login = input('Login (a-z): ')
user_password = int(input('Password (0-9): '))

print(variant_1(user_profiles, user_login, user_password))
print(variant_2(user_profiles, user_login, user_password))
