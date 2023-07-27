#파이썬 조합
import itertools

n, m = map(int, input().split())
a = list(map(int, input().split()))

List = itertools.combinations(a, 3) #리스트 a에서 중복없이 3개 추출

maxi = 0

for i in List:
    if sum(i) <= m:
        maxi = max(maxi, sum(i))

print(maxi)