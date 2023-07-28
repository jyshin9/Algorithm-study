import sys

n = int(input())
x = []

for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    x.append((a, b))

y = sorted(x, key = lambda x:x[0])

for i in y:
    print(i[0], i[1])