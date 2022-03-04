# from math import sqrt
from random import randrange

a = []
n = 10
print('Заполненный список:')
for i in range(n):
    number = randrange(100) - 50
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
summa, pr = 0, 1
sumpol = 0
for i in range(n):
    summa += a[i]
    pr *= a[i]
    if a[i] > 0:
        sumpol += a[i]
print('Сумма всех элементов равна', summa)
print(pr)
sr=summa/n
print('Сумма положительных элементов равна', sumpol)