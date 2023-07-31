# for문 사용
# n = int(input())
# a = []

# for i in range(1, 1000000):
#     i = str(i)
#     if(i.rfind('666')!=-1): #'666'이 문자열 안에 있다면
#         a.append(i)

# print(a[n-1])

# while문 사용 - 브루트포스
n = int(input())
th = 1
count = 0

while True:
    if '666' in str(th): 
        count += 1
    if count == n:
        print(th)
        break
    th += 1