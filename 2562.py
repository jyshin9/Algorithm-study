lst = [int(input()) for _ in range(9)]

print(max(lst))

#for i in range(8):
#    if(lst[i] == max(lst)):
#        print(i+1)
#    else:
#        continue

print(lst.index(max(lst))+1)
