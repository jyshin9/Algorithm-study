n, m = map(int, input().split())
board = []
result = []

#2차원 배열로 입력받기
for _ in range(n):
    board.append(input())

# 8*8 크기로 맞춰진 배열 row*col
for row in range(n-7): #가로행 row
    for col in range(m-7): #검사해야하는 횟수 세로열 col
        #W->B 패턴인지 B->W 패턴인지 검사
        changes_WB = 0
        changes_BW = 0

        #8*8로 맞춰진 배열 속 검사
        for i in range(row, row+8):
            for j in range(col, col+8):
                if(i+j)%2 == 0:
                    if board[i][j] != 'B':
                        changes_WB += 1
                    if board[i][j] != 'W':
                        changes_BW += 1
                else:
                    if board[i][j] != 'W':
                        changes_WB += 1
                    if board[i][j] != 'B':
                        changes_BW += 1
        
        result.append(changes_WB)
        result.append(changes_BW)

print(min(result))