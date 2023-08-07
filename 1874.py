import sys
input = sys.stdin.readline
stack, result = [], []
find = True

n = int(input())

now = 1
for i in range(n):
    m = int(input())
    while now <= m:
        stack.append(now)
        result.append('+')
        now += 1
    #pop하기
    if stack[-1] == m:
        stack.pop()
        result.append('-')
    else:
        find = False

if not find: #불가능하다면
    print('NO')
else:
    for i in result:
        print(i)