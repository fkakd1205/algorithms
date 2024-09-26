N = int(input())
P = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]

dp[0][0] = P[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1] + P[i], dp[i-1][0])
    dp[i][1] = max(dp[i-1][0] - P[i], dp[i-1][1])

print(max(dp[N-1][0], dp[N-1][1]))
