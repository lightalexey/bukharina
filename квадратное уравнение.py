a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a!=0:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('действительных корней нет')
    else:
        if d == 0:
            x = (-b + d ** (1 / 2)) / (2 * a)
            print('x1=x2=', x)
        else:
            x1 = (-b + d ** (1 / 2)) / 2 / a
            x2 = (-b - d ** (1 / 2)) / 2 / a
            print('x1=', x1, 'x2=', x2)
else:
    if b != 0:
        x = -c / b
        print("x=", x)
    else:
        print("b=0")
