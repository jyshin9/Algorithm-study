a = []; b = [3]

for i in range(15):
    a.append(i+1)
    b.append(b[i]+2**(i+1))
 
n = int(input())

p = b[n-1]**2

print(p)
