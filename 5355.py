n = int(input())

for _ in range(n):
    a = list(map(str, input().split()))
    num = 0
    for i in range(len(a)):
        if i == 0:
            num += float(a[i]) #미친 이런방법이
        else:
            if a[i] == '@':
                num *= 3
            elif a[i] == '%':
                num += 5
            elif a[i] == '#':
                num -= 7

    print("%.2f" %num)