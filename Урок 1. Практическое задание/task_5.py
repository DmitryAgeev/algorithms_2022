"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StackPlates:
    def __init__(self, max_size):
        self.plate_list = []
        self.new_plate_list = []
        self.max_of_plates = max_size

    def stack_size(self):
        return len(self.plate_list)

    def push_in(self, count):
        self.plate_list.append(count)
        while self.stack_size() > self.max_of_plates:
            self.new_plate_list.append(self.plate_list[:self.max_of_plates])
            self.plate_list = self.plate_list[self.max_of_plates:]

    def all_stack_size(self):
        return self.new_plate_list + self.plate_list


if __name__ == '__main__':

    folding = StackPlates(5)

    for i in range(1, 14):
        folding.push_in(i)
        print(folding.all_stack_size())
