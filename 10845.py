n = int(input())
queue = []
result = []

for _ in range(n):
    comm = input()

    if comm.startswith("push"):
        _, value = comm.split()
        queue.append(value)
    elif comm == 'pop':
        if queue == []:
            result.append(-1)
        else:
            result.append(queue.pop(0))
    elif comm == 'size':
        result.append(len(queue))
    elif comm == 'empty':
        if queue == []:
            result.append(1)
        else:
            result.append(0)
    elif comm == 'front':
        if queue == []:
            result.append(-1)
        else:
            result.append(queue[0])
    elif comm == 'back':
        if queue == []:
            result.append(-1)
        else:
            result.append(queue[-1])

for i in result:
    print(i)