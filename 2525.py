h,m = map(int, input().split())
c = int(input())

mm = m+c

if(mm<60):
    print(h,mm)
elif(mm==60):
    if(h==23):
        print(0,0)
    else:
        print(h+1,0)
else: #mm>60
    if(h==23):
        print(mm//60-1, mm%60)
    else:
        print(h+mm//60, mm%60)
    
