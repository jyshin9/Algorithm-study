a = []

for _ in range(5):
    a.append(list(input()))

#print(a)
#[['A', 'A', 'B', 'C', 'D', 'D'], ['a', 'f', 'z', 'z'], ['0', '9', '1', '2', '1'], ['a', '8', 'E', 'W', 'g', '6'], ['P', '5', 'h', '3', 'k', 'x']]
#이런식으로 문자열 사이에 공백이 없어도 잘 들어가 있음

max_len = 0

for i in range(5):
    if len(a[i]) > max_len:
        max_len = len(a[i])

for j in range(max_len):
    for k in range(5):
        if j < len(a[k]):
            print(a[k][j], end = "")
        else: #만약 최대길이의 리스트보다 길이가 짧다면
            pass
        
