n = int(input())

def fac(a):
    fac_output = 1
    for i in range(1, a+1):
        fac_output *= i
    return fac_output

if n == 0 :
    print(1)
else:
    print(fac(n))