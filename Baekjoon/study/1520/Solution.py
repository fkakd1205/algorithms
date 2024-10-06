from sys import stdin, setrecursionlimit

setrecursionlimit(10**9)

N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if (x, y) == (N-1, M-1):
        return 1
    
    # dp[x][y] != -1이라면 이미 방문한 곳으로, 이미 재귀를 통해 (N-1, M-1) 도달 여부를 확인했다
    # 따라서 다음 블럭을 실행하지 않고, 이미 구한 값을 이용해 바로 리턴하면 된다.
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < M and arr[cx][cy] < arr[x][y]:
                dp[x][y] += dfs(cx, cy)
    
    return dp[x][y]

dfs(0, 0)
print(dp[0][0])
