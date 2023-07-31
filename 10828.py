#스택 - 리스트 사용

n = int(input())
stack = []
result = []

def push(n):
    stack.append(n)

def pop():
    if stack == []:
        result.append(-1)
    else:
        result.append(stack.pop())

def top():
    if stack == []:
        result.append(-1)
    else:
        result.append(stack[-1])

def size():
    result.append(len(stack))

def empty():
    if stack == []:
        result.append(1)
    else:
        result.append(0)

for _ in range(n):
    comm = input()

    if comm.startswith("push"):
        _, value = comm.split()
        push(value)
    elif comm == 'pop':
        pop()
    elif comm == 'top':
        top()
    elif comm == 'size':
        size()
    else:
        empty()

for i in result:
    print(i)