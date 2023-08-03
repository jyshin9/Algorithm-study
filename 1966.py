from collections import deque #deque 함수
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    tqueue = deque(map(int, input().split())) #큐 선언 후 집어넣을 값 입력받기
    init = deque(x for x in range(len(tqueue))) #초기 인덱스값
    target = tqueue[b]
    th = 0 #몇번째로 출력되는지
    
    while True:
        if tqueue[0] == max(tqueue): #i가 젤 크다면 => 출력해야함
            if tqueue[0] == target and init[0] == b: #몇번째로 인쇄되는지 궁금한 친구라면
                th += 1
                print(th)
                tqueue.clear()
                break
            else: 
                tqueue.popleft()
                init.popleft()
                th += 1
        else: 
            tqueue.append(tqueue[0])
            tqueue.popleft()
            init.append(init[0])
            init.popleft()