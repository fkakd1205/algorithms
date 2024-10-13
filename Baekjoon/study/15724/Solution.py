from sys import stdin

N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0] * (M+1)] + [([0] + [0] * M) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
