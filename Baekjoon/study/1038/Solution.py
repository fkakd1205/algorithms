from itertools import combinations

N = int(input())
nums = [i for i in range(10)]
cnt = 0
result = []

for i in range(1, 11):
    for comb in combinations(nums, i):
        li = list(comb)
        li.sort(reverse=True)
        result.append(int(''.join(map(str, li))))

# 0, 1, 2, ... , 10, 20, 30, ... , 21, 31, 41, ...
# -> 0, 1, 2, ..., 10, 20, 21, 30, 31, 32, ...
result.sort()

if len(result) > N:
    print(result[N])
else:
    print(-1)
