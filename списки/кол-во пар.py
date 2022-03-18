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
k=0
for i in range(n-1):
    if (a[i]+a[i+1])%2==0:
        k+=1
print(k)