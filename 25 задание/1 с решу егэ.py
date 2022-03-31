d1 = 0
d2 = 0
k = 0
for x in range(174457, 174506):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            d2 = d1
            d1 = i
            k += 1
    if k == 2:
        print(d1, d2, d1 * d2)
    k = 0
