from sys import stdin
from copy import deepcopy
from collections import deque

N, M = map(int, input().split())
mount = [list(map(int, stdin.readline().split())) for _ in range(N)]
next_mount = deepcopy(mount)
year = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < M and not visited[cx][cy]:
                if mount[cx][cy] <= 0:
                    next_mount[x][y] -= 1
                else:
                    visited[cx][cy] = True
                    q.append((cx, cy))

while True:
    visited = [[False] * M for _ in range(N)]
    seperated_cnt = 0

    for i in range(N):
        for j in range(M):
            if mount[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                seperated_cnt += 1
    
    if seperated_cnt >= 2:
        break
    elif seperated_cnt == 0:
        year = 0
        break

    # deepcopy로 진행한다면 시간초과 발생
    for i in range(N):
        for j in range(M):
            if mount[i][j] != 0:
                mount[i][j] = next_mount[i][j]
    year += 1

print(year)
