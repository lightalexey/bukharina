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
