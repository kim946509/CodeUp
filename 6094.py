n = int(input())
a = input().split()
for i in range(0, n):
    a[i] = int(a[i])
min = a[0]
for i in range(1, n):
    if min > a[i]:
        min = a[i]
print(min)
