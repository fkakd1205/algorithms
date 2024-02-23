from sys import stdin
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
arr = []
visited = []

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < M and not visited[cx][cy] and arr[cx][cy] == 1):
                q.append((cx, cy))
                visited[cx][cy] = True
        

T = int(input())
for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        arr[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if (arr[i][j] == 1 and not visited[i][j]):
                count += 1
                bfs(i, j)

    print(count)
        