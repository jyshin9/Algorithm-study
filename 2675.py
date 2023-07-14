n = int(input())

num, a = [input().split() for _ in range(n)]
num = int(num)

for i in range(n):
    for j in range(len(a)-1):
        print(a[j], end ="")*num
    
