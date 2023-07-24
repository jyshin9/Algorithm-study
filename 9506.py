a, b = [],[]

while True:
    n = int(input())
    if n == -1:
        break

    for i in range(1, n):
        if n%i == 0: a.append(i)
        else: pass
    
    if sum(a) == n:
            b.append(str(n) + " = " + " + ".join(str(i) for i in a))
    else:
        b.append(str(n) + " is NOT perfect.") #+를 사용할거면 int형 n을 str로 변경해주어야함. str(n)
        
    a.clear()  #다음입력을 위하여 list a를 clear

for i in range(len(b)):
    print(b[i])