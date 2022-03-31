d1 = 0
d2 = 0
k = 0
s = 0
for x in range(245690, 245757):
    s += 1
    for i in range(1, x+1):
        if x % i == 0:
            d2 = d1
            d1 = i
            k += 1
    if k == 2:
        print(s, x)
    k = 0