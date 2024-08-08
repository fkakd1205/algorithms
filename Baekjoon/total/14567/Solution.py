from sys import stdin

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
dp = [1] * (N+1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    arr[b].append(a)

for i in range(1, N+1):
    if len(arr[i]) == 0: continue
    for prev in arr[i]:
        dp[i] = max(dp[i], dp[prev])
    dp[i] += 1

print(*dp[1:])
