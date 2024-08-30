from sys import stdin
from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, stdin.readline().split())) for _ in range(N)]
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = -1

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < N and 0 <= cy < M and tomato[cx][cy] == 0:
                tomato[cx][cy] = tomato[x][y] + 1
                q.append((cx, cy))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))

bfs()

for line in tomato:
    if 0 in line:
        answer = -1
        break
    answer = max(answer, max(line) - 1)

print(answer)
            