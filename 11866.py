#deque(원형큐) 사용
import sys
from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

re = []
while len(queue) != 0:
    for _ in range(k-1):
        queue.append(queue.popleft())
    re.append(str(queue.popleft()))

output = "<" + ", ".join(re) + ">"

print(output)