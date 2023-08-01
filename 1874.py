n = int(input())
a = [] #만들어야하는 리스트
b = [] #1부터n까지 리스트
c = [] #새 리스트

for i in range(n):
    a.append(int(input()))
    b.append(i+1)

for i in a:
    for j in b:
        while j != i:
            b.pop()
            print('-')
        c.append(j)
        print('+')
        
