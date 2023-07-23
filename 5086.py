word = []

while True:
    a, b = map(int, input().split())
    if a ==0 and b ==0:
        break
    elif b % a == 0:
        word.append('factor')
    elif a % b == 0:
        word.append('multiple')
    else:
        word.append('neither')

for i in range(len(word)):
    print(word[i])