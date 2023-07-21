n = int(input())

line = 0 #수가 있는 라인(사선)
end = 0 #라인의 마지막 인덱스(ex. 1,3,6,..)

while n > end:
    line += 1
    end += line

gap = end - n

if line%2 == 0: #라인이 짝수번째 일 때
    top = line - gap
    under = gap + 1
else: #라인이 홀수번째 일 때
    top = gap + 1
    under = line - gap

print("%d/%d"%(top, under))