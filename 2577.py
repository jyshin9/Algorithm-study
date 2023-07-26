a = int(input())
b = int(input())
c = int(input())

d = str(a*b*c)
nums = [0] * 10

for j in range(len(d)):
    for i in range(10):
        if int(d[j]) == i:
            nums[i] = int(nums[i]) + 1

for i in range(len(nums)):
    print(nums[i])