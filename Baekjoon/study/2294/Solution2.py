from sys import stdin

INF = int(1e6)
n, k = map(int, input().split())
coins = [int(stdin.readline().rstrip()) for _ in range(n)]
dp = [0] + [INF] * k

coins.sort()

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
