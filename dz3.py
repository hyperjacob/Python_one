print("_____Задание 1______")
def delenie(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return print("На ноль делить нельзя")
    return c

number1 = float(input("Введите делимое: "))
number2 = float(input("Введите делитель: "))
print("Результат деления: ", delenie(number1, number2))

print("_____Задание 2______")

def userdata(name, surname, year, city, mail, phone):
    print(f"Имя: {name}; Фамилия: {surname}; Год рождения: {year}; Город проживания: {city}; E-mail: {mail}; Телефон: {phone}")

userdata(name = "Алексей", surname = "Иванов", city = "Свердловск", year = "1999", phone = "+79990098765", mail = "ivanov@mail.ru")

print("_____Задание 3______")

def my_func(a, b, c):
    if (a<b) and (a<c):
        return b + c
    elif (b<a) and (b<c):
        return a + c
    elif (c<a) and (c<b):
        return a + b
    else:
        return a+b+c
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))

print(f"Сумма наибольших двух аргументов: {my_func(number1,number2,number3)}")

print("_____Задание 4______")

def stepen(x, y):
    result = 1
    for i in range(abs(y)):
        result = result * x
    return 1 / result

def stepen2(x, y):
    return x**(-(abs(y)))

x = float(input("Введите  действительное положительное число, возводимое в степень: "))
y = int(input("Введите отрицательный показатель степени: "))

print(f"{x} в степени -{abs(y)} = {stepen(x,y)}")
print(f"{x} в степени -{abs(y)} = {stepen2(x,y)}")

print("_____Задание 5______")
def numbersum(str, sum):
    num = str.split(" ")
    result = 0
    i = None
    for el in num:
        try:
           result += int(el)
        except:
            if el == "!":
                return result+sum, False
            else:
                print(f"{el} - такого символа я не знаю, продолжайте ввод")
                return result+sum, True
    return result+sum, True

sum = 0
F = True
while F:
    string = input("Введите числа через пробел, для завершения наберите '!': ")
    temp = numbersum(string, sum)
    sum = temp[0]
    F = temp[1]
    if F:
        print(f"Промежуточная сумма: {sum}")
print(f"Финальное число: {sum}")

print("_____Задание 6 и 7 (вариант 1)______")
def int_func2(text):
    return text.title()

text = input("Введите строку: ")
print("Результат: ", int_func2(text))

print("_____Задание 6 (вариант 2)______")
def int_func(text):
    first = True
    result = ""
    for el in text:
        if first == True:
            result += el.upper()
            first = False
        else:
            result += el
    return result

text2 = input("Введите слово: ")
print("Результат: ", int_func(text2))

print("_____Задание 7 (вариант 2)______")
def int_func_str(text):
    word = text.split(" ")
    result = ""
    for el in word:
        result += int_func(el)+" "
    return result

text3 = input("Введите предложение: ")
print("Результат: ", int_func_str(text3))