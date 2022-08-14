r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
n = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            n += 1
print(n)
