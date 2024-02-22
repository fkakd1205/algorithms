from sys import stdin
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
q = deque()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 큐에 익은 토마토들의 좌표를 넣어둔다
for i in range(N):
    for j in range(M):
        if(arr[i][j] == 1):
            q.append((i, j))

def bfs():
    while q:
        x, y = q.popleft()
    
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < M):
                if (arr[cx][cy] == 0):
                    arr[cx][cy] = arr[x][y] + 1
                    q.append((cx, cy))

bfs()

date = 0
completed = True
for x in range(N):
    for y in range(M):
        if (arr[x][y] == 0):
            completed = False
            break
        date = max(date, arr[x][y])
    if not completed: break

if not completed:
    print(-1)
else:
    if date == 1:
        print(0)
    else:
        print(date-1)

