n, m = map(int, input().split())

box = [0] * n

for i in range(n):
    box[i] = str(i+1)

for i in range(-1, m-1):
    a, b = map(int, input().split())
    temp = box[a-1:b]
    temp.reverse()
    box[a-1:b]=temp

print(" ".join(box))
