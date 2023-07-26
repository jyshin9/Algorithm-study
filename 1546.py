n = int(input())
a = list(map(int, input().split()))
b = [0]*n

for i in range(n):
    b[i] = (int(a[i]) / max(a))*100

avg = sum(b)/n

print(avg)