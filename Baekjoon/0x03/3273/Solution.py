# from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

# V1. 시간초과 (combinations 사용)
# comb = combinations(nums, 2)

# count = 0
# for a, b in comb:
#     if(a + b == x):
#         count += 1

# print(count)

nums.sort()

st = 0
en = n-1
count = 0
while(st < en):
    sum = nums[st] + nums[en]
    if(sum == x):
        count += 1
        st += 1
    elif(sum > x):
        en -= 1
    else:
        st += 1

print(count)
