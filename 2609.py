def maxi(n, m): #최대공약수
    maxi = 0
    for i in range(1, min(n,m)+1): #와 범위 +1 하나 안했다고 틀림 ;;;
        if n%i ==0 and m%i == 0:
            maxi = max(maxi, i)
    return maxi

def mini(n, m): #최소공배수
    mini = n*m
    for i in range(max(n,m), n*m):
        if i%n == 0 and i%m == 0:
            mini = min(mini, i)
    return mini

n, m = map(int, input().split())

print(maxi(n, m))
print(mini(n, m))