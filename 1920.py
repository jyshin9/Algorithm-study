n = int(input())
list_one = list(map(int, input().split()))
m = int(input())
list_two = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        print('0')
        return
    
    mid_index = (start+end)//2
    middle = array[mid_index]

    if target == middle:
        print('1')
    elif target > middle:
        binary_search(list_one, target, mid_index+1, end)
    elif target < middle:
        binary_search(list_one, target, start, mid_index-1)
    else:
        print('0')

list_one.sort()

for i in list_two:
    binary_search(list_one,i,0,n-1)