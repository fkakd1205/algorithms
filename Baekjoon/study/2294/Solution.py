from sys import stdin

INF = int(1e6)
n, k = map(int, input().split())
coins = [int(stdin.readline().rstrip()) for _ in range(n)]
coins.sort()
dp = [INF] * (k+1)

for coin in coins:
    if coin > k:
        break
    dp[coin] = 1

for num in range(1, k+1):
    for coin in coins:
        if num >= coin: 
            dp[num] = min(dp[num], dp[num - coin] + 1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
