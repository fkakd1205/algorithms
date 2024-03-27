from sys import stdin
from bisect import bisect_left

N = int(input())
card = list(map(int, stdin.readline().split()))
card.sort()

M = int(input())
nums = list(map(int, stdin.readline().split()))
result = []

for i in range(M):
    idx = bisect_left(card, nums[i])
    if idx < N and card[idx] == nums[i]:
        result.append(1)
    else:
        result.append(0)

print(*result)
