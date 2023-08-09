n, m = map(int, input().split())
line, amount = [], 0 

for i in range(n):
    line.append(int(input()))

#
for i in line:
    for j in range(i):
        while i >= 0:
            i -= j
            amount += 1
                        