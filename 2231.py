n = int(input())
a = [] #생성자들을 담아낼 리스트

for i in range(1, n+1):
    summ = i
    for j in range(len(str(i))):
        i = str(i) #int형은 슬라이싱이 안되기 때문에 str로 변경
        summ += int(i[j]) 
    if summ == n:
        a.append(i)

if a == []: #생성자가 없다면
    print('0')
else:
    print(a[0]) #가장 작은 생성자 출력