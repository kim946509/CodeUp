d = []
h, w = input().split()
h = int(h)
w = int(w)
for i in range(h+1):
    d.append([])
    for j in range(w+1):
        d[i].append(0)

n = int(input())
for i in range(n):
    l, k, x, y = input().split()
    k = int(k)
    l = int(l)
    x = int(x)
    y = int(y)
    if k == 0:
        for j in range(l):
            d[x][y+j] = 1
    else:
        for j in range(l):
            d[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(d[i][j], end=' ')
    print()
