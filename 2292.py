room = 1; num = 1; i = 1
n = int(input())

while True:
    num += 6*i
    i += 1
    room += 1
    if n < num:
        print(room)
        break
