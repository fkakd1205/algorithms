from sys import stdin

n = int(input())
num = [int(stdin.readline().rstrip()) for _ in range(n)]
mx = max(num)
dp = [0] * (mx+1)
MOD = 1_000_000_009
dp[1] = 1


if mx > 1:
    dp[2] = 2
if mx > 2:
    dp[3] = 4

for i in range(4, mx+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for i in range(n):
    print(dp[num[i]] % MOD)
