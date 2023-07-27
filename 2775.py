n = int(input())
p = []

for _ in range(n):
    a = [0]*14
    for i in range(1, 15):
        a[i-1] = i

    floor = int(input()) #층
    num = int(input()) #호수

    for _ in range(floor):
        for i in range(1, num):
            a[i] += a[i-1] # 층별 각 호실의 사람 수를 변경
    
    p.append(a[num-1])

    a.clear()

for i in p:
    print(i)