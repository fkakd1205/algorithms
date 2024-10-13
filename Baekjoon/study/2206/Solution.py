from sys import stdin
from collections import deque

INF = int(1e9)
N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
visited = [[[INF] * M for _ in range(N)] for _ in range(2)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

q.append((0, 0, 0))
visited[0][0][0] = 1

while q:
    x, y, cnt = q.popleft()

    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < N and 0 <= cy < M:
            if arr[cx][cy] == 0 and visited[cnt][cx][cy] == INF:
                q.append((cx, cy, cnt))
                visited[cnt][cx][cy] = visited[cnt][x][y] + 1
            elif arr[cx][cy] == 1 and cnt == 0:
                q.append((cx, cy, 1))
                visited[1][cx][cy] = visited[cnt][x][y] + 1

answer = min(visited[0][N-1][M-1], visited[1][N-1][M-1])

if answer == INF:
    print(-1)
else:
    print(answer)
