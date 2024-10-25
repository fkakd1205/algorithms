from sys import stdin

n = int(input())
m = int(input())

vip = [int(stdin.readline().rstrip()) for _ in range(m)]
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
if m > 0:
    pre = 0
    for i in range(m):
        answer *= dp[vip[i] - pre - 1]
        pre = vip[i]
    answer *= dp[n - pre]
else:
    answer = dp[n]

print(answer)
