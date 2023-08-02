import sys
n = int(sys.stdin.readline())
goal = [] #만들어야하는 리스트
begin = [] #1부터n까지 리스트
assist = [] #pop한 원소를 임시로 담아둘

for i in range(n):
    goal.append(int(input()))
    begin.append(i+1)

for i in goal:
    for j in begin:
        if i == j+1:
            assist.pop()
            print('-')
        else: 
            while assist[-1] == j:
                assist.append(j)
                print('+')
