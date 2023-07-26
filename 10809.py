words = list(input())
a = [-1]*26

for i in words:
    for j in range(26):
        if i == chr(j+97):
            a[j] = words.index(i)

for i in a:
    print(i, end = " ")