from sys import stdin

n, k = map(int, input().split())
coins = [int(stdin.readline().rstrip()) for _ in range(n)]
dp = [1] + ([0] * k)

for coin in coins:
    for i in range(1, k+1):
        if i-coin >= 0:
            dp[i] += dp[i - coin]

print(dp)
