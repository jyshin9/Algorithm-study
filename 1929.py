n, m = map(int, input().split())

prime_list = [True] * (m+1) #소수라면 True
prime_list[0] = False #0은 소수가 아님
prime_list[1] = False #1은 소수가 아님

for i in range(2, int(m**0.5)+1):
    if prime_list[i]: #아직 걸러지지 않은 합성수
        for j in range(i*2,m+1,i): #4부터 하면됨(효율up), i가 2라면 2의 배수 전부 거르기(False)
            prime_list[j] = False

for i in range(n, m+1):
    if prime_list[i]: #소수라면
        print(i)