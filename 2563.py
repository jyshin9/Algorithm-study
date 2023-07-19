n = int(input())

paper = [[0 for i in range(101)] for j in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = True #색칠되는 부분을 True라고 해놓기

total = 0 

for i in range(101):
        for j in range(101):
            if paper[i][j]: #True인 면적
                total += 1

print(total)
