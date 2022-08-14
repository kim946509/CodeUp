h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
value = h*b*c*s/8/1024/1024
print(format(value, "0.1f"), "MB")
