a = 'Мама мыла раму'
alpha = 'уеэоаыяию'
k = 0
for i in range(len(a)):
    if a[i] in alpha:
        k += 1
print(k) # 3 способ