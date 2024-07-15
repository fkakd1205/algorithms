# from itertools import combinations
from sys import stdin

N, S = map(int, input().split())
arr = list(map(int, stdin.readline().split()))
answer = 0

# for i in range(1, N+1):
#     p = combinations(arr, i)
#     for nums in p:
#         if sum(nums) == S:
#             answer += 1

# print(answer)

def brute(cur, sum):
    global answer

    if cur == N:
        if sum == S:
            answer += 1
        return

    brute(cur + 1, sum)
    brute(cur + 1, sum + arr[cur])

brute(0, 0)

# S가 0이면 (0, 0) -> (1, 0) -> ... -> (N, 0) 으로 무조건 1개가 더해짐
if S == 0:
    answer -= 1

print(answer)
