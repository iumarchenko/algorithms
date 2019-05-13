import random
import timeit

n = random.randint(10,20)
l = [random.randint(0,10) for i in range (n)]
print(l)

# 4. Определить, какое число в массиве встречается чаще всего.
# вар-т 1
# мы формируем второй массив, по длине равный первому.
# во втором массиве каждый элемент представляет собой количество повторов для соответствующего элемента первого массива
# этот вариант работает медленнее чем второй. тут основная проблема в том, что мы обращаемся к элементу массива через индекс
def alg_1():
    m = [0 for i in range (n)]
    for i in range (n):
        for j in l:
            if j == l[i]:
                m[i] += 1
    max = m[0]
    max_ind = 0
    for i in range (n):
        if m[i] > max:
            max = m[i]
            max_ind = i

    return 'Чаще всего в массиве встречается число {} - {} раз'.format(l[max_ind], max)

# вар-т 2
# тут просто идем по массиву, считаем количество повторов для каждого элемента. потом сравниваем с максимальным количеством повторов.
# этот вариант работает быстрее чем первый.
# тут нет дополнительного массива и на 1 цикл меньше чем в первом варианте
def alg_2():
    max_n = 0
    max_cnt = 0
    for i in l:
        cnt = 0
        for j in l:
            if j == i:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_n = i
    return 'Чаще всего в массиве встречается число {} - {} раз'.format(max_n, max_cnt)

# вар-т 3
# аналогичен второму варианту, разница только в том что во втором варианте "for i in l" + "i/j" а здесь оба цикла "for i in range (n)" + "l[i]/l[j]"
# хотя нет дополнительных переменных, массивов и циклов как в первом варианте, работает медленнее чем первый и сильно медленнее чем второй
# похоже дело действительно в обращении к элементам массива по индексу o_0
def alg_3():
    max_n = 0
    max_cnt = 0
    for i in range (n):
        cnt = 0
        for j in range(n):
            if l[j] == l[i]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_n = l[i]

    return 'Чаще всего в массиве встречается число {} - {} раз'.format(max_n, max_cnt)

print(timeit.timeit("alg_1()", setup="from __main__ import alg_1, n, l", number=10000))
print(timeit.timeit("alg_2()", setup="from __main__ import alg_2, n, l", number=10000))
print(timeit.timeit("alg_3()", setup="from __main__ import alg_3, n, l", number=10000))

# print(alg_1())
# print(alg_2())
# print(alg_3())