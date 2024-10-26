N = int(input())
MOD = 10_007
dp = [[0] * 11 for _ in range(N+1)]

for i in range(1, 11):
    dp[1][i] = 1


for i in range(2, N+1):
    for j in range(11):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

answer = sum(dp[N])
print(answer % MOD)
