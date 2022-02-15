print("______Задание 1______")
class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = []
        for el in my_matrix:
            if self.my_matrix == [] or len(self.my_matrix[0]) == len(el):
                self.my_matrix.append(el)
            else:
                print(f"Строка {el} не принята так как не соответствует по длине")


    def __str__(self):
        matrix = ""
        for el in self.my_matrix:
            for item in el:
                matrix += "   " + str(item)
            if el != self.my_matrix[-1]:
                matrix += "\n\n"
        return matrix

    def __add__(self, outher):
        if len(self.my_matrix) == len(outher.my_matrix) and len(self.my_matrix[0]) == len(outher.my_matrix[0]):
            new_matrix = []
            for i in range(len(self.my_matrix)):
                sum_str = []
                for j in range(len(self.my_matrix[i])):
                    sum_str.append(self.my_matrix[i][j]+outher.my_matrix[i][j])
                new_matrix.append(sum_str)
            return Matrix(new_matrix)
        else:
            print('матрицы несоразмерны')


a = Matrix([[1, -2, 3], [2, 3, 4, 5], [3, 42, 55], [4, 51, 53]])
print(a)
print("+")
b = Matrix([[3, 72, 1], [1 ,77, 753], [2,- 2, -43]])
print(b)
print("=")
print(a+b)
print("Проверка исключений")
c = Matrix([[3, 11, 1], [1 ,4, 3], [2,- 2, -52], [33, 11, 33]])
d = Matrix([[3, 11, 1, 5], [1 ,4, 3, 3], [2,- 2, -52, 33]])
print(c)
print(d)
print(a+c)
print(a+d)

print("______Задание 2______")
from abc import ABC, abstractmethod


class Main(ABC):
    @abstractmethod
    def add_coat(self):
        pass

    @abstractmethod
    def add_suit(self):
        pass

    @abstractmethod
    def common_calc(self):
        pass


class Clothes_abc(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Сlothes(Main):
    name = ""
    cloathers_Suit = []
    cloathers_Coat = []

    def add_coat(self, v):
        self.cloathers_Coat.append(Coat(v))

    def add_suit(self, h):
        self.cloathers_Suit.append(Suit(h))

    @property
    def common_calc(self):
        sum_calc = 0
        for el in self.cloathers_Suit:
            sum_calc += el.squareSuit
        for el in self.cloathers_Coat:
            sum_calc += el.squareCoat
        return sum_calc


class Coat(Clothes_abc):
    def __init__(self, v):
        self.squareCoat = v / 6.5 + 0.5

class Suit(Clothes_abc):
    def __init__(self, h):
        self.squareSuit = 2 * h + 0.3


coat = Coat(5)
print(coat.squareCoat)
suit = Suit(6)
print(suit.squareSuit)

r = Сlothes()
r.add_coat(5)
r.add_suit(6)
r.add_suit(6)
r.add_suit(6)
print(r.common_calc)

print("______Задание 3______")


class Cell:
    str_ryad = ""

    def __init__(self, unit):
        if unit > 0:
            self.unit = int(unit)
        else:
            print("Недопустимое количество ячеек, количество ячеек = 1")
            self.unit = 1


    def __add__(self, other):
        return Cell(self.unit + other.unit)

    def __sub__(self, other):
        if self.unit - other.unit > 0:
            return Cell(self.unit - other.unit)
        else:
            return print("Разность ячеек в клетках меньше 0")

    def __mul__(self, other):
        return Cell(self.unit * other.unit)

    def __truediv__(self, other):
            return Cell(self.unit // other.unit)

    def __str__(self):
        if self.str_ryad:
            return f"Количество ячеек в клетке: {self.unit}. Количество ячеек по рядам:\n" + self.str_ryad
        else:
            return f"Количество ячеек в клетке: {self.unit}"


    def make_order(self, number):
        for el in range(self.unit):
            if (el+1) % number == 0:
                self.str_ryad += "\n"
            else:
                self.str_ryad += "*"
        return self.str_ryad

a = Cell(222)
b = Cell(41)
x = a + b
print(x)
y = a - b
print(y)
z = a / b
print(z)
m = a * b
print(m)
a.make_order(36)
print(a)