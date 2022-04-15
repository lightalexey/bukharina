# Маска 12345?7?8 и должны делиться на 23. Вывести числа и результат деления
for a1000 in range(10):
    for a10 in range(10):
        numb = int('12345'+str(a1000)+'7'+str(a10)+'8')
        if numb%23 == 0:
            print(numb,numb//23)
print('========== 2 способ ============')
for a1000 in range(10):
    for a10 in range(10):
        numb = 123450000 + a1000*1000 +700 + a10*10 + 8
        if numb%23 == 0:
            print(numb,numb//23)
