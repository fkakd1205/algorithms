from sys import stdin
from collections import deque

N = int(input())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
checked = [[False] * N for _ in range(N)]
mx = max(map(max, board))
answer = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, r):
    q = deque()
    q.append((x, y))
    checked[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < N and 0 <= cy < N and not checked[cx][cy] and board[cx][cy] > r:
                checked[cx][cy] = True
                q.append((cx, cy))

for rain in range(mx):
    group = 0
    checked = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not checked[i][j] and board[i][j] > rain:
                bfs(i, j, rain)
                group += 1

    answer = max(answer, group)

print(answer)
