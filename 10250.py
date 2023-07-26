c = int(input())
rooms = []

for i in range(c):
    h, w, n = map(int, input().split())
    
    for j in range(1, w+1):
        for k in range(1, h+1):
            n -= 1
            if n == 0:
                if j >=10:
                    rooms.append(str(k) + str(j))
                else:
                    rooms.append(str(k) + '0' + str(j))
                break
            
for i in rooms:
    print(i)