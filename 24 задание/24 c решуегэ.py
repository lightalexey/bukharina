f = open('24.txt')
a = f.readline()
tek = 1
k =1
#print(a)
for i in range(len(a)-1):
    # if a[i] != a[i + 1] != 'P':
    if a[i] != a[i+1] or a[i+1] != 'P':
    # if a[i] != 'P' and a[i] != 'P':
        tek +=1
    else:
        if tek>k:
            k = tek
        tek = 1
print(max(k,tek))

b = a.split('PP')
maxx = 1
for i in range(len(b)):
    if len(b[i])>maxx:
        maxx = len(b[i])
print(maxx)