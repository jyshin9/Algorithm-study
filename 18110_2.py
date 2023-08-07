from collections import deque
import sys
input = sys.stdin.readline

#일반 round 함수는 사사오입. 오사오입 규칙을 적용한 round함수
def round_(num):
    dec = num - int(num) #소수점
    if dec < 0.5:
        num = int(num)
    else:
        num = int(num) + 1
    return num

n = int(input())

if not n:
    print(0)
else:
    s = deque()
    for _ in range(n):
        s.append(int(input())) #평균낼 값들
    ss = deque(sorted(s))

    trim = round_(0.15*n)

    #슬라이싱
    if trim != 0: 
        ss = list(ss)[trim:-trim] #trim만큼 양끝에서 제거

    result = round_(sum(ss)/len(ss))
    print(result)