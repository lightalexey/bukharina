k = 0
min1 = 0
max1 = 0
for x in range(350000, 1000000):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            min1 = i
            break
    for j in range(x // 2 + 1, 2, -1):
        if x % j == 0:
            max1 = j
            break
    M = max1 - min1
    if M%23 == 9:
        k+=1
        print(x,M)
        if k == 6:
            break
