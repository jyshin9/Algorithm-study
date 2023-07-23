n = int(input())
lst = [list(input()) for i in range(n)]

for i in range(n):
    print(lst[i][0],lst[i][-1],sep="")
    
