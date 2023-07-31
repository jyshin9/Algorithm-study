#스택 - 리스트 사용(함수없이)

n = int(input())
stack = []
result = []

for _ in range(n):
    comm = input()

    if comm.startswith("push"):
        _, value = comm.split()
        stack.append(value)
    elif comm == 'pop':
        if stack == []:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif comm == 'top':
        if stack == []:
            result.append(-1)
        else:
            result.append(stack[-1])
    elif comm == 'size':
        result.append(len(stack))
    else:
        if stack == []:
            result.append(1)
        else:
            result.append(0)

for i in result:
    print(i)