for A in range(1,100):
    f =1
    for x in range(1,1000):
        if (not (not (x%A == 0)) or not (x%6 == 0) or not(x%4 == 0)) == 0:
            f =0
            break
    if f:
        print(A)