print("______Задание 1______")
from sys import argv

script_name, virabotka_h, stavka, premia = argv
zp = int(virabotka_h)*int(stavka)+int(premia)
print("Ваша зарплата:", zp)

print("______Задание 2______")
my_list = [int(i) for i in input("Введите числа через пробел: ").split(" ")]
my_list2 = [el for el in my_list if el > my_list[my_list.index(el)-1] and my_list.index(el) != 0]
print(my_list2)

print("______Задание 3______")
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

print("______Задание 4______")
my_list3 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list4 = [el for el in my_list3 if my_list3.count(el) == 1]
print(my_list4)

print("______Задание 5______")
from functools import reduce


def func(a, b):
    return a * b

my_list5 = [el for el in range(100, 1001) if el % 2 == 0]

proizv = reduce(func, my_list5)
print(proizv)

print("______Задание 6______")
import itertools

number = int(input("Введите число, с которого начать генерацию: "))

for el in itertools.count(number):
    if el > number+20:
        break
    else:
        print(el)

my_list6 = ["Пробка", "Джин", "Лампа", "Аладдин", "Джафар", "Аббу", "Джасмин"]
с = 0
for el in itertools.cycle(my_list6):
    if с > number:
        break
    print(el)
    с += 1

print("______Задание 7______")

def fact(n):
    mult = 1
    for el in range(1, n+1):
        mult *= el
        yield mult
        
n = int(input("Введите число, до которого необходимо сгенерировать ряд факториалов: "))
print(fact(n))
result = [el for el in fact(n)]
print(f"Ряд факториалов до {n}: {result}")
