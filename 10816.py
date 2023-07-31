# 기본으로 품
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = [0]*m

for i in a:
    for j in range(m):
        if i == b[j]:
            result[j] += 1

for i in result:
    print(i, end = "")