n = int(input())
a = []

for i in range(n):
    a.append(sum(map(int, input().split())))

for i in range(n):
    print(a[i])