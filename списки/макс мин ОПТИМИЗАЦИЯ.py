#from math import sqrt
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
maximum = a[0]
minimum = a[0]
imax = 0
for i in range(n):
    if a[i]<minimum:
        minimum = a[i]
    if a[i]>maximum:
        maximum = a[i]
        imax = i
print(maximum, imax)
print(minimum)
print(max(a))
print(min(a))
print(sum(a))