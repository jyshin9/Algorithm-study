output = []

while True:
    a = list(map(int, input().split()))

    if a[0]==0:
        break
    
    if sum(a) <= max(a)*2:
        output.append('Invalid')
    else:
        if a[0]==a[1]==a[2]:
            output.append('Equilateral')
        elif a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
            output.append('Isosceles')
        else:
            output.append('Scalene')
    a.clear()

for i in output:
    print(i)