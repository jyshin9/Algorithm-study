a ,b = map(int, input().split())
c = []

for i in range(1,a+1): #a까지 포함해야함
    if a%i == 0:
        c.append(i)
    else:
        pass

if b > len(c):
    print('0')
else:
    print(c[b-1])