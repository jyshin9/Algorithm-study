n, m = map(int, input().split())

box = [0] * n

for i in range(n):
    box[i] = str(i+1)

for _ in range(-1, m-1):
    a, b = map(int, input().split())
    box[a-1], box[b-1] = box[b-1], box[a-1]

print(" ".join(box))
