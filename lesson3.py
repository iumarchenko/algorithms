import random
print('\nЗадача 1')
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
cnt = [0 for _ in range(2,10)]
for i in range(2,100):
    for j in range(2,10):
        if i % j == 0:
            cnt[j-2] += 1

print(cnt)

print('\nЗадача 2')
# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

n = random.randint(10,20)
l = [random.randint(0,100) for i in range (n)]
print("Исходный список: ", l)
m = []
for i in range (n):
    if l[i] != 0 and l[i] % 2 == 0:
        m.append(i)
print("Полученный список: ", m)


print('\nЗадача 3')
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

n = random.randint(10,20)
l = [random.randint(0,100) for i in range (n)]
print(l)
min = l[0]
max = l[0]
min_ind = 0
max_ind = 0

for i in range (n):
    if l[i] < min:
        min = l[i]
        min_ind = i
    if l[i] > max:
        max = l[i]
        max_ind = i

l[min_ind] = max
l[max_ind] = min

print(l)

print('\nЗадача 4')

# 4. Определить, какое число в массиве встречается чаще всего.
n = random.randint(10,20)
l = [random.randint(0,10) for i in range (n)]
print(l)
m = [0 for i in range (n)]
for i in range (n):
    for j in l:
        if j == l[i]:
            m[i] += 1
print(m)

max = m[0]
max_ind = 0
for i in range (n):
    if m[i] > max:
        max = m[i]
        max_ind = i

print('Чаще всего в массиве встречается число {} - {} раз'.format(l[max_ind], m[max_ind]))

print('\nЗадача 5')
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
n = random.randint(10,20)
l = [random.randint(-100,10) for i in range (n)]
print(l)
max = -100
max_ind = 0
for i in range (n):
    if l[i] < 0 and l[i] > max:
        max = l[i]
        max_ind = i
print('Максимальный отрицательный элемент {}, номер элемента {}'.format(l[max_ind], max_ind))


print('\nЗадача 6')
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

n = random.randint(10,20)
l = [random.randint(0,10) for i in range (n)]
print(l)
min = l[0]
max = l[0]
min_ind = 0
max_ind = 0

for i in range (n):
    if l[i] < min:
        min = l[i]
        min_ind = i
    if l[i] > max:
        max = l[i]
        max_ind = i

sum = 0
if min_ind < max_ind:
    for i in range(min_ind+1, max_ind):
        sum += l[i]
else:
    for i in range(max_ind, min_ind+1):
        sum += l[i]


print('Сумма элементов, ',sum)





