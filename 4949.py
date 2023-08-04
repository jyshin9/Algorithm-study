from collections import deque

while True:
    data = input()
    if data == "." :
        break

    stack = []
    is_balance = True

    for i in data:
        if i == '.':
            break
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(': #스택이 비어있거나 짝이 안맞을때
                is_balance = False
                break
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[': #스택이 비어있거나 짝이 안맞을때
                is_balance = False
                break
            stack.pop()

    if not stack and is_balance:
        print('yes')
    else:
        print('no')