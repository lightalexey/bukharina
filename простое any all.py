n = 11
if all(n % i != 0 for i in range(2, n // 2 + 1)):
    print('простое')
else:
    print('составное')
# any
if any(n % i == 0 for i in range(2, n // 2 + 1)):
    print('составное')
else:
    print('простое')