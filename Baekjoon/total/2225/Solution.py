N, K = map(int, input().split())

dp = [[1] * N] + [[0] * N for _ in range(K-1)]

for i in range(1, K):
    dp[i][0] = i + 1
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[K-1][N-1] % int(1e9))
