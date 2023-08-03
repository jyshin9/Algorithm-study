n = int(input())
m = int(input())

prime_list = [True]*(m+1)
prime_list[0] = False
prime_list[1] = False

for i in range(2, int(m**0.5)+1):
    if prime_list:
        for j in range(2*i,m+1,i):
            prime_list[j] = False

result = []
for i in range(n, m+1):
    if prime_list[i]:
        result.append(i)

if result == []:
    print(-1)
else:
    prime_sum = 0
    for i in result:
        prime_sum += i

    print(prime_sum)
    print(min(result))