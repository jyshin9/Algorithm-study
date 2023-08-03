import sys
input = sys.stdin.readline
end = [[10],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]

def whatisend(a,b):
    Aend = a % 10 
    Bend = b % len(end[Aend])
    if Aend == 10:
        return 0
    else:
        return end[Aend][Bend-1]

for i in range(int(input())):
    a, b = map(int, input().split())
    print(whatisend(a,b))