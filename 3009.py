a, e = map(int, input().split())
b, f = map(int, input().split())
c, g = map(int, input().split())

if a==b!=c: d = c
elif a==c!=b: d = b
elif a!=b==c: d = a

if e==f!=g: h = g
elif e==g!=f: h = f
elif e!=f==g: h = e

print(d, h)