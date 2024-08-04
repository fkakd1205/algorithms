from sys import stdin

INF = int(1e6)
n, k = map(int, input().split())
coins = [int(stdin.readline().rstrip()) for _ in range(n)]
dp = [0] + ([INF] * (k))

for i in range(k+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
