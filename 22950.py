import sys

n = int(sys.stdin.readline())
m = sys.stdin.readline().strip()[::-1] #2진수 입력받고 뒤집기
k = int(sys.stdin.readline())
binary = 0

for i in range(n):
    if m[i] == '1':
        binary += 2**i
        
if binary % (2**k) == 0 :
    print('YES')
else:
    print('NO')