for A in range(1000,1,-1):
    f = 1
    for x in range(1,100):
        for y in range(1,100):
            if (not (x <= 9) or (x**2 <= A) and (not(y**2 <=A) or (y <= 9))) == 0:
                f = 0
    if f:
        print(A)
        break