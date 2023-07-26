n = int(input())
b = []

for _ in range(n):
    a = (list(input()))

    c = int(a[0])
    strr = ''

    for j in range(2, len(a)):
        strr += c*a[j]
     
    b.append(strr)

    strr = '' #strr 초기화
    a.clear() #a 초기화

for i in range(n):
    print(b[i])

#실패작
#n = int(input())

# num, a = [input().split() for _ in range(n)]
# num = int(num)

# for i in range(n):
#     for j in range(len(a)-1):
#         print(a[j], end ="")*num 