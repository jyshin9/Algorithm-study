import sys
input = sys.stdin.readline

n = int(input())

def fibonacci(n):
    if n == 0:
        return 0, 1
    elif n == 1:
        return 1, 0
    else:
        p_zero, p_one = fibonacci(n-1)
        p2_zero, p2_one = fibonacci(n-2)
        return p_zero + p2_zero, p_one + p2_one

for _ in range(n):
    fib = int(input())
    zero_count, one_count = fibonacci(fib)
    print(one_count, zero_count)