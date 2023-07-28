n = int(input())
p, r = [], []

for i in range(n):
    x, y = map(int,input().split())
    p.append((x,y))

for i in p:
    rank = 1
    for j in p:
        if i[0]<j[0] and i[1]<j[1]:
            rank += 1
    r.append(rank)

for i in r:
    print(i, end =" ")