#совершенные числа с делителями
x = int(input())
for i in range(1,x//2+1):
  if x%i == 0:
    print(i, end = ' ')
print()

#факториал числа
y = int(input())
a = 1
for i in range(1,y+1):
  a*=i
print(a)