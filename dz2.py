print("______Задание 1______")
my_list = [4, 55, "cat", True, 0.55, "FFF", {4, 55, 99}, (0.44, 12), [44, 22]]
print(f"Исходный массив: {my_list}")
for el in my_list:
    print(el, type(el))

print("______Задание 2______")
input_list = input("Введите элекменты списка через пробел: ")
my_list_2 = input_list.split()
for i in range(0, len(my_list_2), 2):
    try:
        my_list_2[i], my_list_2[i+1] = my_list_2[i+1], my_list_2[i]
    except IndexError:
        break
print(my_list_2)

print("______Задание 3______")
mounth = {12: "Зима", 1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень"}
try:
    my_list_3 = int(input("Введите месяц (числом): "))
except ValueError:
    print("Вы ввели не целое число")
    exit(0)
print(f"Ваш месяц отностится к времени года: {mounth[my_list_3]}")

print("______Задание 4______")
my_list_4 = input("Введите строку из нескольких слов: ")
slovar = my_list_4.split()
for ind, el in enumerate(slovar, 1):
    print(ind, el[:10] if len(el) > 10 else el)

print("______Задание 5______")
first_list = [7, 5, 3, 3, 2]
first_list.append(int(input("Введите число для рейтинга:")))
first_list.sort(reverse=True)
print(first_list)

print("______Задание 6______")
i=0
structure = []
shablon = {}
n = int(input("введите количество товаров, которые собираетесь добавить: "))
for i in range(n):
    print(f"Введите данные о товаре №{i+1}")
    shablon["название"] = input("Введите название товара: ")
    shablon["цена"] = int(input("Введите цену товара: "))
    shablon["количество"] = int(input("Введите количества товара: "))
    shablon["ед"] = input("Введите единицу измерения количества товара: ")
    temp = (i+1, shablon.copy())
    structure.append(tuple(temp))
print(f"Вы ввели: {structure}")
names = []
cost = []
numb = []
unit = []
for i in range(n):
    names.append(structure[i][1]["название"])
    cost.append(structure[i][1]["цена"])
    numb.append(structure[i][1]["количество"])
    unit.append(structure[i][1]["ед"])
analitics = {"название": names, "цена": cost, "количество": numb, "ед": unit}
print(f"Аналитика: {analitics}")

