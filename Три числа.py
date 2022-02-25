a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > b and c > a:
    print(c)
print(max(a,b,c))