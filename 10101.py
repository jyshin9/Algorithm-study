a = int(input())
b = int(input())
c = int(input())

sum_angle = a + b + c

if sum_angle == 180:
    if a == b == c:
        print('Equilateral')
    elif a==b!=c or a!=b==c or a==c!=b:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')