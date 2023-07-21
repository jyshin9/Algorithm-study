n = int(input())
a = [25, 10, 5, 1]
r = []

for i in range(n):
    m = int(input()) #거스름돈 입력

    for i in range(4):
        r.append(int(m//a[i]))
        m -= a[i]*(m//a[i])
    
for i in range(0, n*len(a), 4):
    print(*r[i:i+4])

# unpacking기능
# *은 [1, 2, 3, 4] 이렇게 출력될 것을 1 2 3 4 이렇게 출력되게 해줌.