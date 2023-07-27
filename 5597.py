a = list(range(1, 31))
b, c = [], []

for _ in range(28):
    b.append(int(input()))

for num in a:
    if num not in b:
        c.append(num)
sorted(c)

for i in c:
    print(i)