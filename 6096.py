b = []
for i in range(20):
    b.append([])
    for j in range(20):
        b[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        b[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    for j in range(1, 20):
        if b[j][y] == 0:
            b[j][y] = 1
        else:
            b[j][y] = 0

        if b[x][j] == 0:
            b[x][j] = 1  # 아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ==을발견못해서.........
        else:
            b[x][j] == 0


for i in range(1, 20):
    for j in range(1, 20):
        print(b[i][j], end=' ')
    print()
