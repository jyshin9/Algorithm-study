def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

a, b = map(int, input().split())
re = fac(a)//(fac(b)*fac(a-b))

print(re)