croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  #input 변수와 동일한 이름의 변수, croatia 안에 들어있는 문자를 만나면 '*'로 변경
print(len(word))