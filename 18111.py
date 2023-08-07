import sys

input = sys.stdin.readline
n, m, b = map(int, sys.stdin.readline().split())
answer = sys.maxsize
idx = 0

arr = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
	
for floor in range(257): #층
    exceed_block, lack_block = 0, 0 #제거, 추가 해야하는 블럭 수

    for col in range(n): #열(세로)
        for row in range(m): #행(가로)
            if arr[col][row] >= floor:
                exceed_block += arr[col][row] - floor
            else:
                lack_block += floor - arr[col][row]
    
    if exceed_block + b >= lack_block:
        if (exceed_block * 2) + lack_block <= answer:
            answer = (exceed_block * 2) + lack_block
            idx = floor

print(answer, idx)