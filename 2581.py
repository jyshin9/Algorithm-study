n = int(input())
m = int(input())
a = []
sum_num = 0

for i in range(n, m+1):
    for j in range(2, i+1):
        if i%j != 0: 
            continue
        else: #나누어떨어지면
            sum_num += 1
    
    if sum_num == 1: #본인에 의하여 나누어 떨어진다면(소수)
        a.append(i)

    sum_num = 0 #다음 반복문을 위하여 sum_num값 초기화 !!!

if len(a) > 0:
    print(sum(a))
    print(a[0])
else:
    print("-1")