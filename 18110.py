from collections import deque

n = int(input())
s = deque() #사용자 의견 난이도

for _ in range(n):
    s.append(int(input()))
ss = deque(sorted(s)) #오름차순으로 정렬
jeolsa = round(n * 0.15)

for _ in range(jeolsa):
    ss.popleft()
    ss.pop()
    
if len(ss) == 0:
    result = 0
else:
    result = round(sum(ss)/len(ss))

print(result)