from sys import stdin

N, K = map(int, input().split())
bagpack = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = bagpack[i-1]
    for j in range(K+1):
        if j - w >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
