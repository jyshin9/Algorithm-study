# 이분탐색으로 구현하기
_ = int(input())
lst = list(map(int, input().split()))
lst.sort() #오름차순 정렬하기
_ = int(input())

def binary_search(array, target, first, last):
    if first > last:
        return 0
    
    middle_idx = (first+last)//2
    middle = array[middle_idx]

    if target == middle:
        return array[first:last+1].count(target)
    elif target > middle:
        return binary_search(array, target, middle_idx+1, last)
    elif target < middle:
        return binary_search(array, target, first, middle_idx-1)
    else:
        return 0

lst2 = list(map(int, input().split()))

result = {} #딕셔너리 선언
for j in lst:
    if j not in result:
        result[j] = binary_search(lst, j, 0, len(lst)-1)

print(' '.join(str(result[x]) if x in result else '0' for x in lst2 ))