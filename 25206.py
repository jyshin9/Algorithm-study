#sum = 0
#
#for _ in range(20):
#    a, b, c = input().split()
#    if c == "A+" : s = float(b) * 4.5
#    elif c == "A0" : s = float(b) * 4.0
#    elif c == "B+" : s = float(b) * 3.5
#    elif c == "B0" : s = float(b) * 3.0
#    elif c == "C+" : s = float(b) * 2.5
#    elif c == "C0" : s = float(b) * 2.0
#    elif c == "D+" : s = float(b) * 1.5
#    elif c == "D0" : s = float(b) * 1.0
#    elif c == "F" : s = float(b) * 0.0
#    else: s = 0.0
#
#    sum += s
#
#score = sum/20
#
#print(score)

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
sum = 0

for i in range(20):
    a, b, c = input().split()
    if(c == rating[i-1]):
        total = float(total) * grade[i-1]
        sum += total
    elif c == 'P'
        sum
    else:
        pass
    
