from sys import stdin

n = int(input())
arr = [0] + [int(stdin.readline().rstrip()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n+1)]
dp[1][1] = arr[1]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]

print(max(dp[n]))
