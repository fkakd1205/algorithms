from sys import stdin

n, k = map(int, input().split())
coins = [int(stdin.readline().rstrip()) for _ in range(n)]
dp = [1] + ([0] * k)
coins.sort()

for coin in coins:
    for i in range(coin, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(dp[k])
