import string

str = input().upper()

alpha = list(string.ascii_uppercase)
s = [0]*26
    
for i in range(len(str)):
    for j in range(len(alpha)):
        if str[i] == alpha[j]:
            s[j] += 1

max_alpha = max(s)

if s.count(max_alpha) == 1:
    print(alpha[s.index(max_alpha)])
else: #가장 많이 등장한 단어가 하나가 아니라면
    print("?")
