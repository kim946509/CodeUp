d = []

for i in range(10):
    d.append([])
    for j in range(10):
        d[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        d[i][j] = int(a[j])
print()
print('------------------------')
x, y = 1, 1
while x != 9 or y != 9:

    if d[y][x] == 2:
        d[y][x] = 9
        break
    d[y][x] = 9
    if x != 9 and y != 9:
        if d[y][x+1] != 1:
            x = x+1
        else:
            if d[y+1][x] != 1:
                y = y+1
            else:
                d[y][x] = 9
                break
    elif x == 9:
        if d[y+1][x] != 1:
            y = y+1
        else:
            d[y][x] = 9
            break
    elif y == 9:
        if d[y][x+1] != 1:
            x = x+1
        else:
            d[y][x] = 9
            break
for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
