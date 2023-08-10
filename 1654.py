#이분탐색
# def binary(arr, target, start, end):
#     if end > start:
#         return False
    
#     mid_index = (start+end)//2 #중앙값
#     mid = arr[mid_index]
    
#     if mid == target:
#         return True
#     elif mid > target:
#         return binary(arr, target, start, mid-1)
#     elif mid < target:
#         return binary(arr, target, mid+1, end)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
amount = 0

line = [int(input()) for _ in range(n)]

for i in line: #오영식이 가지고 있는 랜선의 길이
    for j in range(i): 
        while i >= 0: #랜선이 사라지기 전까지
            i -= j
            amount += 1
                        