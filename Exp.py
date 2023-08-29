class Exceptions(Exception):
    pass


class MinLengthError(Exceptions):

    def __init__(self, param, value):
        self.param = param
        self.value = value

    def __str__(self):

        if self.param < self.value:
            return f'Сторона треугольника не может быть меньше нуля\n' \
                   f'Заданное число {self.param} < {self.value}'
        elif self.param == self.value:
            return f'Сторона треугольника не может быть равна нулю\n' \
                   f'Заданное число {self.param} = {self.value}'


class TriangleError(Exceptions):

    def __init__(self, value1: int, value2: int, value3: int):
        self.a = value1
        self.b = value2
        self.c = value3

    def __str__(self):
        print(f"Tреугольника со сторонами {self.a}, {self.b}, {self.c} не существует!")