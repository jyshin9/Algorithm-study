x, y, w, h = map(int, input().split())
a = w-x; b = h-y

lst = [x, y, a, b]

print(min(lst))
