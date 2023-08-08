n = int(input())
result = []

num = 0

for _ in range(n):
    a = list(input().split())
    
    if type(a[0]) == 'int':
        num = int(a[0])
    elif type(a[0]) == 'float':
        num = float(a[0])

    for i in range(len(a)):
        if a[i] == '@':
            num *= 3
            round(num, 2)
        elif a[i] == '%':
            num += 5
            round(num, 2)
        elif a[i] == '#':
            num -= 7
            round(num, 2)

    result.append(round(a[0],2))

for i in result:
    print(i)