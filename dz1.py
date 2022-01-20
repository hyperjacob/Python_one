print('______Задание 1______')
a = 20
b = "Привет"
v = {"Name": "Вася", "Age": 25}
print(f"{b}, Вы {a} пользователь системы! До Вас системой пользовался {v['Name']}, ему {v['Age']}")
v['Name'] = input("Введите Ваше имя: ")
v['Age'] = int(input("Введите Ваш взраст: "))
print(f"Вас зовут {v['Name']}, Вам {v['Age']}")

print('______Задание 2______')
time = int(input("Введите время секундах: "))
s = time % 60
m = ((time - s)/60) % 60
h = time // 3600
print("Вы ввели: %(hour)d часов, %(min).0f минут и %(sec)d секунд." % {"hour":h, "min": m,"sec": s})

print('______Задание 3______')
number = input("Введите число: ")
number2 = number*2
number3 = number*3
sum = int(number) + int(number2) + int(number3)
print(f"{number} + {number}{number} + {number}{number}{number} = {sum}")

print('______Задание 4______')
number = input("Введите целое положительное число: ")
i = 0
max_number = 0
z = len(number)
while z > i:
    if (int(number) % 10) > max_number:
        max_number = (int(number) % 10)
    number = number[:-1]
    i += 1
print(f"Самое большое число в строке: {max_number}")

print('______Задание 5______')
vir = int(input("Введите выручку Вашей компании: "))
izd = int(input("Введите издержки Вашей компании: "))
if vir > izd:
    print("Компания работает с прибылью")
elif vir == izd:
    print("Компания работает 'в ноль'")
elif izd > vir:
    print("Компания работает в убыток")

print('______Задание 6______')
if vir > izd:
    print(f"Рентабельность Вашей компании: {(vir-izd)/vir}")
    num_s = int(input("Введите число сотрудников фирмы: "))
    if num_s > 0:
        print(f"Прибыль фирмы в расчете на 1го сотрудника: {(vir-izd)/num_s}")
    else:
        print("Число сотрудников не может быть меньше одного")
else:
    print("Задание 6 выполено: прибыль не обнаружена")

print('______Задание 7______')
a1 = int(input("Введите сколько км спортсмен должен пробежать за первый день: "))
b1 = int(input("Введите сколько км спортсмен должен пробежать всего: "))
day = 1
while a1 < b1:
    if a1 >= b1:
        break
    else:
        day += 1
        a1 = 1.1 * a1
print(f"За {day} день спортсмен достиг результата - не менее {b1} км")