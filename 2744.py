words = input()
answer = ""
for i in words:
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)