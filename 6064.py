a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if a < b else b) if ((a if a < b else b) < c) else c
print(d)
# 입력받은 값은 바로 원하는 자료형으로 전환하는 버릇 가지기
# 오류 계속 못찾았음...
