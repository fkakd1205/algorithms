N = int(input())
dp = [0] * (N+1)
dp[0] = 1

if N % 2 == 0:
    for i in range(2, N+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(4, N+1, 2):
            if i < j: break
            dp[i] += dp[i-j] * 2

print(dp[N])
