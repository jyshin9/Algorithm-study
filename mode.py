n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

def times(array): #최빈값
    count_dict = {}
    for num in array:
        count_dict[num] = count_dict.get(num, 0) +1 #key값 등장 횟수마다 value값 1씩 증가
    
    max_count = max(count_dict.values())
    
    modes = [] #최빈값을 담을 리스트
    for i in count_dict:
        if count_dict.items() == max_count:
            modes.append(i)
    modes.sort()
    print(modes)
    
    if len(modes) >= 2:
        return modes[1]
    elif len(modes) == 1:
        del 
    else: #최빈값이 없다면

print(times(a))