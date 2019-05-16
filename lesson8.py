# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib
import random

n = random.randint(10, 20)
alph = "abcdefghijklmnopqrstuvwxyz"
s = ''.join(random.choices(alph, k=n))
print("Исходная строка: ",s)

m = set()
for i in range(1,len(s)):
    for j in range(len(s)-i+1):
        # m.add(s[j:j+i])
        m.add(hashlib.sha1(s[j:j+i].encode('utf-8')).hexdigest())
        # print("i: {}, j: {}, str: {}".format(i,j,s[j:j+i]))

print("Количество различных подстрок в  строке: ", len(m))

