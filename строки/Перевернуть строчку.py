a = 'Мама мыла раму'
b = []
k = len(a) #1 способ перевернуть строку
while k > 0:
    b += a[k - 1]
    k -= 1
print(b)

print(a[::-1]) #2 способ перевернуть строку

a = a.replace(' ', '')
print(a) # избавились от пробелов

c = []
n = int(input())
for i in range(n):
    e = input()
    c.append(e)
print()
for i in range(n):
    print(c[i], end=' ')
print()
print(c)
s = 0
for i in a:
    if i in c:
        s += 1
print(s) #1 способ

d = []
for i in a:
    if i in c:
        d.append(i)
print(len(d)) #2 способ


k = 0
for i in range(len(a)):
    if a[i] in alpha:
        k += 1
print(k) # 3 способ