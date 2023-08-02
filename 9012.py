n = int(input())
stack = []
result = []

for _ in range(n):
    flag = 0 #끝까지 0을 지켜낸다면 VPS 맞음
    stack.clear()
    n = input()
    for b in n:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if stack == []:
                flag = 1 # 빈스택에 ')'이 들어왔다면 VPS 아님! 
            else:
                stack.pop()
    if flag == 0 and stack == []: #다 짝이 맞아 빠져나가 스택이 비어있어야함
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)