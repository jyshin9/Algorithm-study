a = []
max_ = 0

for i in range(9):
    i = list(map(int, input().split()))
    a.append(i)

for j in range(9):
    for k in range(9):
        if a[j][k] > max_ :
            max_ = a[j][k]

print(max_)

for j in range(9):
    for k in range(9):
        if a[j][k] == max_ :
            print(j + 1, k + 1)
