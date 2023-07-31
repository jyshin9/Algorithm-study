# Deque
import sys
from collections import deque

n = int(input())
dq = deque()
result = deque()

for _ in range(n):
    comm = sys.stdin.readline().split()

    if comm[0] == "push_front":
        dq.appendleft(comm[1])
    elif comm[0] == "push_back":
        dq.append(comm[1])
    elif comm[0] == 'pop_front':
        if dq == deque([]):
            result.append(-1)
        else:
            result.append(dq.popleft())
    elif comm[0] == 'pop_back':
        if dq == deque([]):
            result.append(-1)
        else:
            result.append(dq.pop())
    elif comm[0] == 'size':
        result.append(len(dq))
    elif comm[0] == 'empty':
        if dq == deque([]):
            result.append(1)
        else:
            result.append(0)
    elif comm[0] == 'front':
        if dq == deque([]):
            result.append(-1)
        else:
            result.append(dq[0])
    else:
        if dq == deque([]):
            result.append(-1)
        else:
            result.append(dq[-1])

for i in result:
    print(i)