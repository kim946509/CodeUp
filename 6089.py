a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)
if n == 1:
    print(a)
else:
    print(r**(n-1)*a)
