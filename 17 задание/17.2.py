#39762
f = open('17.2.txt')
n = 5542
a = []
k = 0
number = 0
summax = 0
for i in range(n):
    number = int(f.readline())
    a.append(number)
for i in range(len(a) - 1):
    if (a[i] * a[i+1]) % 15 == 0:
        if (a[i] + a[i + 1]) % 7 == 0:
            k += 1
            if a[i] + a[i+1] > summax:
                summax = a[i] + a[i+1]

print(k,summax)
