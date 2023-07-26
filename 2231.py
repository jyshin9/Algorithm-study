n = int(input())
sum_n = 0

for i in range(n):
    sum_n += i
    for j in range(i):
        sum_n += i[j]

    if sum_n == i:
        print(i)