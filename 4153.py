r = []

while True:
    a = list(map(int, input().split()))
    a.sort()

    if sum(a) == 0:
        break
    
    if a[2]**2 == a[1]**2 + a[0]**2:
        r.append('right')
    else:
        r.append('wrong')

for i in r:
    print(i)