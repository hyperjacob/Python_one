print("-----Задание 1-------")
import time

class TrafficLight:
    __color = ""
    def running(self):
        i = 0
        while i < 3:
            self.__color = "Красный"
            print("Светофор переключился на:", self.__color)
            time.sleep(7)
            self.__color = "Желтый"
            print("Светофор переключился на:", self.__color)
            time.sleep(2)
            self.__color = "Зеленый"
            print("Светофор переключился на:", self.__color)
            time.sleep(10)
            i += 1

a = TrafficLight()
a.running()

print("-----Задание 2-------")
class Road:
    _length = 0
    _width = 0
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calcmass(self, mass, thickness):
        self._mass = mass
        self._thickness = thickness
        return str((self._mass * self._thickness * self._length * self._width) / 1000) + " Тонн"

b = Road(20, 5000)
result = b.calcmass(25, 50)
print(result)


print("-----Задание 3-------")
class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

c = Position("Roy", "Kent", "Manager", 100, 50)

print(c.name)
print(c.surname)
print(c.position)
print(c._income)
fullName = c.get_full_name()
totalIncome = c.get_total_income()
print(fullName)
print(totalIncome)


print("-----Задание 4-------")
class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False
    way = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        self.way = True
        print("Машина поехала")

    def stop(self):
        self.way = False
        print("Машина остановилась")

    def turn(self, direction):
        if self.way:
            print("Машина повернула", direction)
        else:
            print("Машина не может повернуть так как стоит на месте")

    def show_speed(self):
        if self.way:
            print(f"Ваша скорость {self.speed} км/ч")
        else:
            print("Машина стоит")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60 and self.way:
            print(f"Вы превышаете скорость на {self.speed-60} км/ч")
        elif self.way:
            print(f"Ваша скорость {self.speed} км/ч")
        else:
            print("Машина стоит")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40 and self.way:
            print(f"Вы певышаете скорость на {self.speed-40} км/ч")
        elif self.way:
            print(f"Ваша скорость {self.speed} км/ч")
        else:
            print("Машина стоит")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


car1 = TownCar(70, "red", "BMW")
car1.show_speed()
car1.go()
car1.show_speed()
car1.turn("направо")
print(car1.is_police)
car1.stop()

car2 = SportCar(150, "green", "Lotos")
car2.show_speed()
car2.go()
car2.show_speed()
car2.turn("налево")
print(car2.color)
car2.stop()

car3 = WorkCar(50, "black", "MAN")
car3.show_speed()
car3.go()
car3.show_speed()
car3.turn("назад")
print(car3.name)
car3.stop()

car4 = PoliceCar(200, "Special", "Ford")
car4.is_police = True
car4.show_speed()
car4.turn("влево")
car4.go()
car4.show_speed()
print(car4.is_police)
car4.stop()

print("-----Задание 5-------")
class Stationery:
    title = "канцелярская принадлежность"
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом")

class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")

st0 = Stationery()
print(st0.title)
st0.draw()

st1 = Pen()
st1.title = "Ручка"
print(st1.title)
st1.draw()

st2 = Pencil()
st2.title = "Карандаш"
print(st2.title)
st2.draw()

st3 = Handle()
st3.title = "Маркер"
print(st3.title)
st3.draw()