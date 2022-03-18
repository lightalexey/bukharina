def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n>2:
        return F(n-1)*F(n-2) +(n-2)

print(F(5))