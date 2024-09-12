from sys import stdin
from collections import deque

M, N, H = map(int, input().split())
tomato = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()
has_zero = False
answer = -1

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1:
                q.append((i, j, k))

while q:
    x, y, z = q.popleft()

    for i in range(6):
        cx = x + dx[i]
        cy = y + dy[i]
        cz = z + dz[i]

        if 0 <= cz < H and 0 <= cx < N and 0 <= cy < M and tomato[cz][cx][cy] == 0:
            tomato[cz][cx][cy] = tomato[z][x][y] + 1
            q.append((cx, cy, cz))

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 0:
                has_zero = True
            if answer < tomato[k][i][j]:
                answer = tomato[k][i][j]

if has_zero:
    answer = -1
elif answer == -1:
    answer = 0
else:
    answer -= 1

print(answer)