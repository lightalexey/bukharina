# a1 a2 a3
a = []
print('Исходный пустой список:')
print(a)
n = int(input('Введи количество элементов:'))
for i in range(n):
    number = int(input('Введи элемент:'))
    a.append(number)
print('Заполненный список:')
for i in range(n):
    print(a[i], end=' ')
print()
print(a)