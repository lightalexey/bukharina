x = int(input())
k = True
for i in range(2, x // 2 + 1):
    if x % i == 0:
        k = False
        break
if k == True:
    print('простое')
else:
    print('составное')
