x = int(input())
k = 0
for i in range(1, x // 2+1):
    if x % i == 0:
        k+=i
if k == x:
    print('да')
else:
    print('нет')