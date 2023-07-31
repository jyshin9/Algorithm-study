# 이분탐색을 구현해보자! - 재귀
def binary_search(array, target, start, end):
    middle_idx = (start+end)//2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        print('answer: {}'.format(middle_idx))
    elif middle > target:
        binary_search(array, target, start, middle_idx-1)
    elif middle < target:
        binary_search(array, target, middle_idx+1, end)
    else:
        return False
    
target = int(input())
t_list = list(map(int, input().split())) #array

t_list.sort() #이진탐색을 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
length = len(t_list)

start = 0; end = length-1

binary_search(t_list, target, start, end)
