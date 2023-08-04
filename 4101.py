while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b: #break문 다음에는 새로운 if문을 시작해야함.
        print("YES")
    else:
        print("NO")