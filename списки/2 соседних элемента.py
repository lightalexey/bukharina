#from math import sqrt
from random import randrange
a = []
n = 10
print('Заполненный список:')
for i in range(n):
    number = randrange(11)
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
a1=a[0]
a2=a[1]
for i in range(n-1):
    if a[i]+a[i+1]>a1+a2:
        a1=a[i]
        a2=a[i+1]
print(a1,a2)