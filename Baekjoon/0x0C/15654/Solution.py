from sys import stdin
from itertools import permutations

# V1. 백트래킹
# N, M = map(int, input().split())
# nums = list(map(int, stdin.readline().split()))
# arr = [0] * N
# isused = [False] * N

# def func(cur):
#     if cur == M:
#         result = []
#         for i in range(M):
#             result.append(arr[i])
#         print(*result)
#         return
    
#     for i in range(N):
#         if isused[i]: continue
#         arr[cur] = nums[i]
#         isused[i] = True
#         func(cur + 1)
#         isused[i] = False

# nums.sort()
# func(0)

# V2. permutations 사용
N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
nums.sort()
comb = permutations(nums, M)

for c in comb:
    print(*c)