def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2

n = int(input())

a = []

for _ in range(n):
    a.append(input())
    
a = sorted(a)
a = Sorting(a)

element_unique = []
for element in a:
    if element not in element_unique:
        element_unique.append(element)

for i in range(len(element_unique)):
    print(element_unique[i])