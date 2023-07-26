n = int(input())
score = [0]*n

for i in range(n):
    count = 0
    a = list(input())
    
    for j in a:
        if j == 'O':
            count += 1
            score[i] = int(score[i]) + count
        else:
            count = 0 # X를 만나면 count다시 초기화! omg!!! 이런 간단한 방법이 .....
        

for i in score:
    print(i)