a = []

while True:
    n = list(input())
    if n == ['0']: break

    if n == n[::-1]: a.append('yes')
    else: a.append('no')

for i in a:
    print(i)