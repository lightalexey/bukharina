f = open('24_demo (1).txt')
s = f.readline()
k = 1
tek = 1
for i in range(len(s)-1):
    if s[i] == s[i+1] == 'X':
        tek += 1
    else:
        if tek > k:
            k = tek
        tek = 1
if tek > k:
    k = tek
print(k)