n = int(input())
fac = 1

for i in range(1, n+1): fac *= i

fac = str(fac)[::-1]
index = 0

for i in fac: 
    if i == '0': index += 1
    else: break #0이 아닌 걸 만나면 끝내버려라

print(index)