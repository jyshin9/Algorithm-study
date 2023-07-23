n, m = map(int, input().split())

arr1, arr2 = [], []

for i in range(n): #arr1배열 가로 길이 n   
	i = list(map(int, input().split()))
	arr1.append(i)

for j in range(n):   
	j = list(map(int, input().split()))
	arr2.append(j)
	
for k in range(n):
    for l in range(m):
        print(arr1[k][l]+arr2[k][l], end = " ")
    print()


