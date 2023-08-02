import sys

n = int(sys.stdin.readline())
a = []

for _ in range(n):
    a.append(int(sys.stdin.readline()))

print(round(sum(a)/len(a))) #산술평균 #반올림 round

a.sort()
mid_idx = len(a)//2
print(a[mid_idx]) #중앙값

#딕셔너리 사용 최빈값
mode = dict() #dictionary 선언
for i in a:
    if i in mode:
        mode[i] += 1
    else:
        mode[i] = 1
mc = max(mode.values()) #max_count
md = [] #최빈값 숫자들을 저장할 배열 max_dict

for i in mode: 
    if mc == mode[i]: #최빈값이 여러개인 상황
        md.append(i)

md.sort()
if len(md) > 1: #최빈값이 여러개라면
    print(md[1]) #두번째로 작은값 출력
else: #하나라면
    print(md[0])

print(a[-1]-a[0]) #범위