# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random

# вар-т 1 - ухудшение. максимальное количество обходов. всегда от начала и до конца
def bubble_1(a):
    cnt = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            cnt += 1
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print('\nКоличество шагов по упорядочению {}'.format(cnt))


# вар-т 2 - пузырьковая сортировка
def bubble_2(a):
    cnt = 0
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            cnt += 1
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print('\nКоличество шагов по упорядочению {}'.format(cnt))

# вар-т 3 - прервемся если перестановок не было
def bubble_3(a):
    cnt = 0
    flag = 0
    for i in range(len(a) - 1, 0, -1):
        flag = 0
        for j in range(i):
            cnt += 1
            if a[j] > a[j+1]:
                flag = 1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
        if flag == 0:
            break
    print('\nКоличество шагов по упорядочению {}'.format(cnt))

# вар-т 4 - шейкерная сортировка

def bubble_4(a):
    cnt = 0
    k = 0
    for i in range(len(a) - 1, 0, -1):
        # выталкиваем наибольший вправо
        for j in range(k, i, 1):
            cnt += 1
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

        # выталкиваем наименьший влево
        for k in range(j, len(a) - j - 2, -1):
            cnt += 1
            if a[k] < a[k - 1]:
                temp = a[k]
                a[k] = a[k-1]
                a[k-1] = temp

        if k >= i - 1:
            break
    print('\nКоличество шагов по упорядочению {}'.format(cnt))



n = random.randint(20,50)
print("Длина массива {}".format(n))
numbers = [random.randint(-100,100) for i in range (n)]
print("Исходный массив {}".format(numbers))

n_1 = numbers.copy()
bubble_1(n_1)
print('Упорядоченный массив 1: {}'.format(n_1))


n_2 = numbers.copy()
bubble_2(n_2)
print('Упорядоченный массив 2: {}'.format(n_2))

n_3 = numbers.copy()
bubble_3(n_3)
print('Упорядоченный массив 3: {}'.format(n_3))

n_4 = numbers.copy()
bubble_4(n_4)
print('Упорядоченный массив 4: {}'.format(n_4))