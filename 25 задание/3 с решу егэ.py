d1 = 0
d2 = 0
d3 = 0
d4 = 0
k = 0
for x in range(210235, 210300):
    for i in range(2, x//2+1):
        if x % i == 0:
            d4 = d3
            d3 = d2
            d2 = d1
            d1 = i
            k += 1
    if k == 4:
        print(d1, d2, d3, d4)
    k = 0