n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    a.append((x,y)) #튜플 ()

b = sorted(a, key = lambda x:(x[1], x[0])) #튜플의 y 정렬, 이후 같은 값이 나오면 x 정렬

for i in b:
    print(i[0], i[1])