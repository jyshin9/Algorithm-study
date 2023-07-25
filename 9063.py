n = int(input())
a, x, y = [], [], []

for i in range(n):
    a.append(list(map(int,input().split())))
    x.append(a[i][0])
    y.append(a[i][1])

rec_x = max(x) - min(x)
rec_y = max(y) - min(y)

print(rec_x * rec_y)