n = int(input())

while (n>0):
    try:
        a , b = map(int, input().split())
        print(a+b)
        n-=1
    except:
        break
    
