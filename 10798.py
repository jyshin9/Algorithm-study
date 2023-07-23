import sys

a = [[0 for i in range(15)]for j in range(15)] #list a 선언

for i in range(5):
    for j in range(15):
        a[i][j] = list(input())

print(a)