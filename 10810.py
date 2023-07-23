n, m = map(int, input().split())
box = [0] * n

for _ in range(m):
    j, k ,l = map(int, input().split())
    for i in range(j-1, k):
            box[i]=l

for a in range(n):
    print(box[a], end=" ")
