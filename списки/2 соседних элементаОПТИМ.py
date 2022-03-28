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
ind=0
for i in range(n-1):
    if a[i]+a[i+1]>a[ind]+a[ind+1]:
        ind=i
print(a[ind],a[ind+1])