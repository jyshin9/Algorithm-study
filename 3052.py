b = []

for i in range(10):
    a = int(input())

    if a%42 not in b :
        b.append(a%42) #b배열에 나머지값을 요소로 추가

print(len(b)) #b배열 길이 출력
