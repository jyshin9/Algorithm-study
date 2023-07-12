str = input()
list = list(str)

for i in range (1, len(str)-1):
    if(str[i-1] == str[len(str)-i]):
       print('1')
       break;
    else:
        print('0')
        break;
