print('Моя первая программа')
print('Как тебя зовут?')
name = input()
print('Рад познакомиться,', name, '!')
age = int(input('Сколько тебе лет?'))
year = 2022 - age
print('Значит ты родился в ', year, 'году!')

a = int(input('Введи а='))
b = int(input('Введи b='))
if a > b:
    print('a>b')
else:  # а меньше или равно b
    if a == b:
        print('числа равны')
    else:
        print('a меньше b')
