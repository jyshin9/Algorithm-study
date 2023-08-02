import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    c = 0
    a, b = map(int, sys.stdin.readline().split())
    c = (a**b) % 10
    result.append(c)

for i in result:
    print(i)