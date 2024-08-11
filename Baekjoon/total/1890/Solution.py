from sys import stdin

N = int(input())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] and board[i][j]:
            k = board[i][j]
            if i + k < N:
                dp[i + k][j] += dp[i][j]
            if j + k < N:
                dp[i][j + k] += dp[i][j]

print(dp[N-1][N-1])
