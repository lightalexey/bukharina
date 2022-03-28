f = open('24_demo.txt')
s = f.readline()
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
k = 1
tek = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:  # цепочка растёт....
        tek += 1
    else: # текущая цепочка оборвалась
        if tek > k:
            k = tek  # k = max(k, tek)
        tek = 1
if tek > k:
    k = tek
print(k)
# print(max(k, tek))