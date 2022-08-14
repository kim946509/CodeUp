w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)
value = w*h*b/8/1024/1024
print(format(value, "0.2f"), "MB")
