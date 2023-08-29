from Exp import MinLengthError, TriangleError


class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise MinLengthError(a, 0)
        if b > 0:
            self.b = b
        else:
            raise MinLengthError(b, 0)
        if c > 0:
            self.c = c
        else:
            raise MinLengthError(c, 0)

    def check_sides(self):

        check1 = self.a + self.b
        check2 = self.a + self.c
        check3 = self.b + self.c
        if (check1 < self.c or check2 < self.b or check3 < self.a):
            raise TriangleError(self.a, self.b, self.c)
        else:
            if (a == b and b == c and c == a):
                print("Треугольник равносторонний")
            elif (a == b or b == c or c == a):
                print("Треугольник равнобедренный")
            else:
                print("Треугольник разносторонний")



if __name__ == "__main__":
    TEXT = f"Введите длинну стороны треугольника "
    try:
        a = int(input(TEXT + "№1: "))
        b = int(input(TEXT + "№2: "))
        c = int(input(TEXT + "№3: "))
    except ValueError as v:
        print(f"Нужно задать число: {v}")

    t1 = Triangle(a, b, c)
    t1.check_sides()
