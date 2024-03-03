from sys import stdin
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
year = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < M and not visited[cx][cy]):
                if arr[cx][cy] > 0:
                    q.append((cx, cy))
                    visited[cx][cy] = True
                else:
                    count[x][y] += 1

while(True):
    visited = [[False] * M for _ in range(N)]
    count = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    # 녹은만큼 빙산의 높이를 빼준다
    for i in range(N):
        for j in range(M):
            if(count[i][j] > 0):
                arr[i][j] -= count[i][j]

    # 빙산이 분리되었다면
    if(cnt > 1):
        print(year)
        break
    
    # 모든 빙산이 녹았다면
    if(cnt == 0):
        print(0)
        break

    year += 1
