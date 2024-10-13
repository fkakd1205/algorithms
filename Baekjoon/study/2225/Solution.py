INF = int(1e9)
N, K = map(int, input().split())
dp = [[0] * (N+1)] + [([1] + [0]*N) for _ in range(K)]

# 6을 4개로 나타낸다면 (0 + (6을 4개로 나타낸 것)) + (1 + (5를 4개로 나타낸 것)) + (2 + (4를 4개로 나타낸 것)) + ...
# 즉, N을 2개로 나타낸다면 (0 + (N을 1개로 나타낸 것)) + (1 + (N-1을 1개로 나타낸 것)) + ...
for i in range(1, K+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[K][N] % INF)
