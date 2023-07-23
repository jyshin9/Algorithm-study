n = int(input())

words = []
cnt = n

for i in range(n):
    words = str(input())

    for j in range(len(words)-1):
        if words[j]==words[j+1]:
            pass
        elif words[j] in words[j+1:]: #[j+1]이후에 [j]와 같은게 있다면
            cnt -= 1
            break

print(cnt)
            
    
    

