N = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(i-1, i//2-1, -1):
        if i-j > 0:
            dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])
