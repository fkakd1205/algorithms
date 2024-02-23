from sys import stdin
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            cz = dz[i] + z
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < M and 0 <= cz < H):
                if (arr[cz][cx][cy] == 0):
                    q.append((cz, cx, cy))
                    arr[cz][cx][cy] = arr[z][x][y] + 1

# 1. 익은 토마토를 모두 큐에 넣는다
for k in range(H):
    for i in range(N):
        for j in range(M):
            if(arr[k][i][j] == 1):
                q.append((k, i, j))

# 2. 익은 토마토를 기준으로 bfs 진행
bfs()

# 3. 토마토 검사
is_completed = True
date = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if(arr[k][i][j] == 0):
                is_completed = False
            date = max(date, arr[k][i][j])

if not is_completed:
    print(-1)
elif date == 1:
    print(0)
else:
    print(date-1)
