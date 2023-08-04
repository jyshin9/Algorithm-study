# a, b, m = map(int, input().split())
# h = 0
# d = 1

# for _ in range(m):
#    h += a
#    if h >= m:
#        print(d)
#        break
#    h -= b
#    d += 1

#올라가야할 거리 m-b
#하루동안 올라갈 수 있는 거리 a-b
a, b, m = map(int, input().split())
k = (m-b)/(a-b)
print(int(k) if int(k)==k else int(k)+1)