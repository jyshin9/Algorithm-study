n = int(input())
a = input()
r = 31; M = 1234567891
b = [0] * n
sum = 0

for i in range(len(a)):
    b[i] = ord(a[i]) - 96
    sum += b[i] * (r ** i)

print(sum%M)