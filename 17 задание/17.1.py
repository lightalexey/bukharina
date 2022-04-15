f = open('17.txt')
n = 10000
a = []
k = 0
summax = 0
for i in range(n):
    number = int(f.readline())
    a.append(number)
# print(len(a))
min17 = 10 ** 6
for j in range(n):
    if a[j]<min17 and a[j] %17 == 0:
        min17 = a[j]
for i in range(n-1):
    if a[i] %min17 == 0 or a[i+1] %min17 == 0:
        k+=1
        if a[i] + a[i+1]>summax:
            summax = a[i] + a[i+1]
print(k, summax)