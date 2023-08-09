n = int(input())
hi = input()
hiarc = [0]*5

for i in hi:
    if i == 'H':
        hiarc[0] += 1
    elif i == 'I':
        hiarc[1] += 1
    elif i == 'A':
        hiarc[2] += 1
    elif i == 'R':
        hiarc[3] += 1
    elif i == 'C':
        hiarc[4] += 1

print(min(hiarc))