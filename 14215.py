a = list(map(int, input().split()))
a.sort() #리스트 a를 오름차순으로 정렬

if a[2] >= a[1] + a[0] : #삼각형이 되는 조건을 만족하지 않으면! #a[0] >= a[1] + a[2]
    while a[2] >= a[1] + a[0]: #크거나 같은 동안~ 꼐속 실행
        a[2] -= 1

print(sum(a))