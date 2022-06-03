a = []
k = 0
f = open('поляков10.txt')
n = int(f.readline())
#print(n)
for i in range(n):
    a.append(int(f.readline()))
#print(*a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]%2 == a[j]%2:
            k+=1
print(k)
k = 0
f.close()
f = open('поляков10.txt')
n = int(f.readline())
for i in range(n):
    if int(f.readline())%2 == 0:
        k+=1
print(k*(k-1)//2 + (n-k)*(n-k-1)//2)
