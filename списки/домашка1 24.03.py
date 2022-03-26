#произведение которых кратно 6
from random import randrange
a = []
n = 4
print('Заполненный список:')
for i in range(n):
    number = randrange(10)
    a.append(number)
    print(a[i], end=' ')
print()
k = 0
for i in range(1, n):
    for j in range(0, i):
        if (a[i] * a[j]) % 6 == 0:
            k += 1
print(k)

#произведение которых кратно 5
from random import randrange
a = []
n = 4
print('Заполненный список:')
for i in range(n):
    number = randrange(10)
    a.append(number)
    print(a[i], end=' ')
print()
k = 0
for i in range(1, n):
    for j in range(0, i):
        if (a[i] * a[j]) % 5 == 0:
            k += 1
print(k)

# сумма которых четная
from random import randrange
a = []
n = 4
print('Заполненный список:')
for i in range(n):
    number = randrange(10)
    a.append(number)
    print(a[i], end=' ')
print()
k = 0
for i in range(1, n):
    for j in range(0, i):
        if (a[i]%2==0 and a[j]%2==0) or (a[i]%2==1 and a[j]%2==1):
            k += 1
print(k)

#сумма которых кратна 6
from random import randrange
a = []
n = 4
print('Заполненный список:')
for i in range(n):
    number = randrange(10)
    a.append(number)
    print(a[i], end=' ')
print()
k = 0
for i in range(1, n):
    for j in range(0, i):
      if (a[i]+a[j])%6==0:
        k+=1
print(k)