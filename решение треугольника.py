a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a+b>c and b+c>a and a+c>b:
    #print("треугольник существует")
    if a==b==c:
        print('треугольник равносторонний')
    elif a==b or b==c or a==c:
            print('треугольник равнобедренный')
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
        print('треугольник прямоугольный')
    else:
        print('реугольник произвольный')
else:
    print('треугольник построить нельзя')