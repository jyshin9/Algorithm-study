output = []

def sum(a, b, c, d, e):
        s = 6*a + 3*b + 2*c + 1*d +2*e
        return s

for i in range(2):
        a,b,c,d,e = map(int, input().split())
        output.append(sum(a, b, c, d, e))

print(*output)
