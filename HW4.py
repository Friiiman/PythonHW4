from random import randint

def task1():
    # Вычислить число c заданной точностью d

    number_first = float(input("Введите число: "))
    number_second = abs(int(input("Введите нужное кол-во знаков после запятой: ")))
    print(f'{number_first:.{number_second}f}')

def task2():
    # Задайте натуральное число N. 
    # Напишите программу, которая составит список простых множителей числа N.

    number = int(input('Введите число: '))
    num = 2
    multiplier = list()
    while num ** 2 <= number:
        while number % num == 0:
            multiplier.append(num)
            number /= num
        num += 1
    if number > 1:
        multiplier.append(int(number))
    print(multiplier)

def task3():
    # Задайте последовательность чисел. 
    # Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

    my_range = int(input('Введите нужное кол-во чисел: '))
    my_list = [randint(0, 3) for _ in range(my_range)]
    print('Сформированный массив: ', my_list)
    for _ in my_list:
        my_list_new = [elem for elem in my_list if my_list.count(elem) == 1]
    if len(my_list_new) != 0:
        print('Массив неповторяющихся элементов: ', my_list_new)
    else:
        print('В массиве нет неповторяющихся элементов')

def task4():
        # Задана натуральная степень k. 
        # Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
        # и записать в файл многочлен степени k.

    number = int(input('Введите натуральную степень k: '))
    if number > 0:
        with open('file.txt', 'w') as data:
            for i in reversed(range(1, number + 1)):
                num = randint(0, 100)
                if num != 0:
                    print(f'{num} * x^{i} +', file = data, end = ' ')
            print(f'{num} = 0', file = data)



task1()
# task2()
# task3()
# task4()
