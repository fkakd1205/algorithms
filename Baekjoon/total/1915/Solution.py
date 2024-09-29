from sys import stdin

n, m = map(int, input().split())
arr = [[0] * (m+1)]+ [[0] + list(map(int, stdin.readline().rstrip())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
answer = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

for i in range(1, n+1):
    answer = max(answer, max(dp[i]))

print(answer ** 2)
