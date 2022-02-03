a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a+b>c:
    if b+c>a:
        if a+c>b:
            print("треугольник существует")
        else:
            print('треугольник построить нельзя')
    else:
        print('треугольник построить нельзя')
else:
    print('треугольник построить нельзя')