print("------Задание 1-------")

with open("file.txt", "w+", encoding="utf-8") as f_obj:
    i = 0
    print("Введите несколько строк текста, для завершения ввод оставьте строку пустой")
    while True:
        i += 1
        text = input(f"Строка {i}: ")
        if text == "":
            break
        f_obj.write(text+"\n")

print("------Задание 2-------")
with open("text_z2.txt", "a") as f_obj:
    f_obj.write('stroka stroka stroka\n')

with open("text_z2.txt", "r", encoding="utf-8") as f_obj:
    i = 0
    for line in f_obj:
        i += 1
        space = line.count(" ")
        word = line.split(" ")
        char = len(line) - space - 1
        number_word = len(word) if char != 0 else 0
        print(f"В {i} строке '{line.rstrip()}': {char} букв и {number_word} слово")

print("------Задание 3-------")
try:
    with open("text_z3.txt", "r", encoding="utf-8") as f_obj:
        full_money = 0
        poor_man = []
        i = 0
        for line in f_obj:
            personal = line.split(" ")
            i += 1
            money = float(personal[1].rstrip())
            if money < 20000:
                poor_man.append(personal[0])
            full_money += money
        print(f"Средняя зарплата сотрудников: {full_money/i}")
        print(f"Список сотрудников с з/п менее 20000 руб: {poor_man}")
except IOError:
    print("Файл text_z3.txt не найден")

print("------Задание 4-------")
import os

os.remove("text-z4_new.txt")
dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open("text_z4.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            word = line.split(" ")
            word[0] = dictionary[word[0]]
            words = ' '.join(word)
            print(words)
            with open("text-z4_new.txt", "a", encoding="utf-8") as r_obj:
                r_obj.write(words)
except IOError:
    print("Файл text_z4.txt не найден")

print("------Задание 5-------")
from random import randint

with open("file2.txt", "w") as f_obj:
    line = [str(randint(0, 20)) for el in range(20)]
    number = " ".join(line)
    f_obj.write(number)
with open("file2.txt", "r") as r_obj:
    line = r_obj.readline()
    numbers = line.split(" ")
    result = 0
    for i in numbers:
        result += int(i)
print("Сумма чисел в файле: ", result)

print("------Задание 6-------")
predmet = {}
number = ""
summa = 0
flag = False
try:
    with open("text_z6.txt", encoding="utf-8") as read_f:
        for line in read_f:
            temp = line.split(":")
            for char in temp[1]:
                if char.isdigit() and flag == True:
                    number += char
                    flag = True
                elif char.isdigit() and flag == False:
                    number = char
                    flag = True
                elif char.isdigit() == False and flag:
                    summa += int(number)
                    flag = False
            predmet.setdefault(temp[0], summa)
            summa = 0
except IOError:
    print("Файл text_z6.txt не найден")
print(predmet)

print("------Задание 7-------")
import json
try:
    with open("text-z7.txt", encoding="utf-8") as read_f:
        profit_sum = 0
        i = 0
        firm_list = {}
        result = []
        for line in read_f:
            firm = line.split(" ")
            profit = int(firm[2])-int(firm[3])
            if profit >= 0:
                profit_sum += profit
                i += 1
            firm_list.setdefault(firm[0], profit)
        average_profit = profit_sum/i
        result.append(firm_list)
        result.append({"average_profit": average_profit})
        print(result)
except IOError:
    print("Файл text-z7.txt не найден")

with open("result_file-z7.json", "w") as write_f:
    json.dump(result, write_f)

