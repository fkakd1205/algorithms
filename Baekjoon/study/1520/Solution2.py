from sys import stdin, setrecursionlimit

M, N = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

setrecursionlimit(10**6)

def dfs(x, y):
    if (x, y) == (M-1, N-1):
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < M and 0 <= cy < N and board[cx][cy] < board[x][y]:
                dp[x][y] += dfs(cx, cy)
    
    return dp[x][y]

dfs(0, 0)
print(dp[0][0])
