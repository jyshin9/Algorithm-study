n = 10000
a = []

for i in range(1, n):
    sum = 0
    i = str(i)
    for j in range(len(i)):
        sum = j
        sum += int(i[j])
    
    if sum == i:
        a.append(i)

for i in a:
    print(i)