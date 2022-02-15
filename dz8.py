print("________Задание 1________")
class Data:
    date = ""

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_include(cls, date):
        day, mounth, year = date.split("-")
        return [int(day), int(mounth), int(year)]

    @staticmethod
    def date_volidation(date):
        day = date[0]
        mounth = date[1]
        year = date[2]
        i = 0

        mounth31 = [1,3,5,7,8,10,12]
        year_v = [2028,   2024,   2020,   2016,   2012,   2008,   2004,   2000,   1996,   1992,   1988,   1984,   1980,   1976,   1972,   1968,   1964,   1960,   1956,   1952,   1948,   1944,   1940,   1936,   1932,   1928,   1924,   1920,   1916,   1912,   1908,   1904]

        if mounth in mounth31 and (day < 1 or day > 31):
            print("Не верно указано число дней в месяце")
        elif mounth == 2 and year in year_v and (day < 1 or day > 29):
            print("Не верно указано число дней в месяце")
        elif mounth == 2 and year not in year_v and (day < 1 or day > 28):
            print("Не верно указано число дней в месяце")
        elif mounth not in mounth31 and mounth != 2 and (day < 1 or day > 30):
            print("Не верно указано число дней в месяце")
        else:
            i += 1

        if (mounth > 12 or mounth < 1):
            print("Месяц указан не верно")
        else:
            i += 1

        if year < 1900:
            print("Год указан не верно")
        else:
            i += 1

        if i == 3:
            return "день, месяц и год указаны верно"
        else:
            return "метод завершился с ошибкой"


print(Data.date_include("22-11-2022"))
print(Data.date_volidation(Data.date_include("22-11-2022")))
print(Data.date_volidation(Data.date_include("29-02-1")))

print("________Задание 2________")
class ExeptionZero(Exception):
    def __init__(self):
        txt = "Делитель не должен быть равен нулю"
        super().__init__(txt)

a = input("Введите делимое: ")
b = input("Введите делитель: ")

try:
    input_a = int(a)
    input_b = int(b)
    if input_b != 0:
        c = input_a/input_b
        print(f"Результат: {c}")
    else:
        raise ExeptionZero
except ValueError:
    print("Вы ввели не число")
except ExeptionZero as err:
    print(err)

print("________Задание 3________")
class ExceptionInt(Exception):
    def __init__(self):
        txt = "Вы ввели не целочисленное значение"
        super().__init__(txt)

number = ""
number_list = []
flag = False

while number != "stop":
    number = input("Введите число для добавления в список (для окончания ввода введите 'stop'): ")
    if number != "" and number[0] == "-":
        number = number[1:]
        flag = True
    try:
        if number.isdigit():
            if flag:
                number = int(number)*(-1)
                flag = False
            else:
                number = int(number)
            number_list.append(number)
        elif number == "stop":
            print("Ввод завершен")
        else:
            raise ExceptionInt
    except ExceptionInt as err:
        print(err)
print(number_list)

print("________Задание 4, 5, 6________")
from abc import ABC, abstractmethod


class ExeptionType(Exception):
    def __init__(self):
        txt = "Необходимо ввести число от 1 до 3"
        super().__init__(txt)

class ExeptionSpeed(Exception):
    def __init__(self):
        txt = "Необходимо ввести целое число"
        super().__init__(txt)

class Sklad:
    onSclad = []
    vidano = {}
    vidan_tech = []
    vidano_num = 0

    def __init__(self, name):
        self.name = name

    def priem(self, item, unit = None):
        if unit is not None:
            if self.vidano.get(unit) is not None:
                self.vidano.get(unit).remove(item)
                self.onSclad.append(item)
                self.vidano_num -= 1
                print(f"На склад поступила следующая техника: {str(item)}, от подразделения: {unit}")
            else:
                print("За этим подразделением в базе ничего не числется")
        else:
            self.onSclad.append(item)
            print(f"На склад поступила следующая техника: {str(item)}")
        return self.onSclad



    def vidacha(self, item, unit):
        if item in self.onSclad:
            self.onSclad.remove(item)
            if self.vidano.get(unit) is not None:
                for el in self.vidano.get(unit):
                    self.vidan_tech.append(el)
                self.vidan_tech.append(item)
                self.vidano[unit] = self.vidan_tech.copy()
                self.vidan_tech.clear()
                self.vidano_num += 1
                print(f"Выдана следующая техника:{str(item)} подразделению: {unit}")
            else:
                self.vidan_tech.append(item)
                self.vidano[unit] = self.vidan_tech.copy()
                self.vidan_tech.clear()
                self.vidano_num += 1
                print(f"Выдана следующая техника:{str(item)} подразделению: {unit}")
        else:
            print("На складе нет такого оборудования")
        return self.vidano

    def __str__(self):
        new_dic = []
        for el in self.vidano.values():
            for el2 in el:
                new_dic.append(str(el2))
        new_dic2 = []
        for el in self.vidano:
            new_dic2.append(el)
        new_dic3 =[]
        i = 0
        for el in self.onSclad:
            i += 1
            new_dic3.append(str(i)+" " + str(el))
        return f'В настоящий момент на складе: {len(self.onSclad)} единиц орг техники: \n {new_dic3} \n Выдана орг техника:  {new_dic} ({self.vidano_num} шт.) подразделениям {new_dic2}'


class Org_tech(ABC):
    quantity = 0
    isTech = True
    color = ""

    def __init__(self, color):
        Org_tech.quantity += 1
        self.color = color

    @abstractmethod
    def __str__(self):
        return f'Наименование: {__name__}, цвет: {self.color}'

    @property
    def num_of_tech(self):
        return f'Количество единиц оргтехники, всего: {Org_tech.quantity} шт'

    @staticmethod
    def new_item_add():
        iserror = True
        while iserror:
            new_item_type = input("Введит тип оргтехники (1 - Xerox, 2 - Принтер, 3 - Сканер): ")
            try:
                if new_item_type.isdigit() and (new_item_type == "1" or new_item_type == "2" or new_item_type == "3"):
                    new_item_type = int(new_item_type)
                    iserror = False
                else:
                    raise ExeptionType
            except ExeptionType as err:
                print(err)
        iserror = True
        while iserror:
            new_item_speed = input("Введите скорость устройства: ")
            try:
                if new_item_speed.isdigit():
                    new_item_speed = int(new_item_speed)
                    iserror = False
                else:
                    raise ExeptionSpeed
            except ExeptionSpeed as err:
                print(err)
        new_item_color = input("Введите цвет устройства:")
        print(new_item_type)
        if new_item_type == 1:
            new_item = Xerox(new_item_speed, new_item_color)
        elif new_item_type == 2:
            new_item = Printer(new_item_speed, new_item_color)
        elif new_item_type == 3:
            new_item = Scanner(new_item_speed, new_item_color)
        print("Вы добавили: ", new_item)

class Printer(Org_tech):
    speed_of_print = 0
    def __init__(self, speed, color):
        self.speed_of_print = speed
        super().__init__(color=color)

    def __str__(self):
        return f'Наименование: {Printer.__name__}, цвет: {self.color}, скорость печати: {self.speed_of_print}'

class Scanner(Org_tech):
    speed_of_scan = 0
    def __init__(self, speed, color):
        self.speed_of_scan = speed
        super().__init__(color=color)

    def __str__(self):
        return f'Наименование: {Scanner.__name__}, цвет: {self.color}'

class Xerox(Org_tech):
    speed_of_copy = 0
    def __init__(self, speed, color):
        self.speed_of_copy = speed
        super().__init__(color=color)

    def __str__(self):
        return f'Наименование: {Xerox.__name__}, цвет: {self.color}'

b = Xerox(34, "red")
c = Scanner(33, "White")
d = Printer(11, "White")
e = Xerox(55, "white")
sklad_main = Sklad("New")
sklad_main.priem(c)
sklad_main.priem(b)
sklad_main.priem(d)
sklad_main.vidacha(b, "Бугалтерия")
sklad_main.vidacha(d, "Отдел кадров")
sklad_main.vidacha(c, "Бугалтерия")
sklad_main.priem(b, "Бугалтерия")
# print(sklad_main)
# print(b.num_of_tech)
print("\n\n\n")

isMenu = True

while isMenu:
    choise = input("Меню:\n 1. Добавить новое устройство \n 2. Закрепить устройство за отделом \n 3. Забрать из отдела на склад \n 4. Завершить программу \n \n Введите номер пункта: ")
    if choise == "1":
        Org_tech.new_item_add()
    elif choise == "2":
        choise2 = input(f"{sklad_main} \n Введите порядковый номер оргтехники для перемещения: ")
        try:
            if choise2.isdigit() and int(choise2) <= len(sklad_main.onSclad):
                choise3 = input("Введите название отдела: ")
                sklad_main.vidacha(sklad_main.onSclad[int(choise2)-1], choise3)
            elif choise2.isdigit() and int(choise2) > len(sklad_main.onSclad):
                print("Вы ввели неправильное число")
            else:
                raise ExeptionType
        except ExeptionType as err:
            print(err)
    elif choise == "3":
        i = 0
        for el in sklad_main.vidano.keys():
            print(f"{el}")
        choise4 = input("Выбирите подразделение: ")
        if choise4 in sklad_main.vidano.keys():

            for el2 in sklad_main.vidano[choise4]:
                i += 1
                print(str(i) + " " + str(el2))
            if i != 0:
                choise5 = input("Введите номер устройства, которое необходимо переместить на склад: ")
                try:
                    if choise5.isdigit() and int(choise5) <= i:
                        sklad_main.priem(sklad_main.vidano[choise4][int(choise5)-1], choise4)
                    elif choise5.isdigit() and int(choise5) > i:
                        print("Вы ввели неправильное число")
                    else:
                        raise ExeptionType
                except ExeptionType as err:
                    print(err)
            else:
                print("За данным подразделением устройств не числится")
        else:
            print("Введено некорректное название")


        i = 0
    elif choise == "4":
        isMenu = False
    else:
        print("Неправильный ввод, повторите попытку")

print("________Задание 7________")
class Complex:
    def __init__(self, im, re):
        self.im = im
        self.re = re

    def __str__(self):
        return f"Комплексное число {self.im} + {self.re}i"

    def __add__(self, other):
        return Complex(self.im + other.im, self.re + other.re)

    def __mul__(self, other):
        return Complex(self.im * other.im - self.re * other.re, self.re * other.im + self.im * other.re)

a = Complex(5, 7)
b = Complex(4, 12)
print(a)
print(b)
print(a * b)
print(a + b)







