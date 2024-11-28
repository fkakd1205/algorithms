from sys import stdin
from collections import deque

INF = int(1e6)
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(H)]
check = [[[INF] * W for _ in range(H)] for _ in range(K+1)]
answer = INF

d1 = [1, -1, 2, -2]
d2 = [-2, 2, 1, -1]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    check[0][0][0] = 0

    while q:
        x, y, cnt = q.popleft()

        if (x, y) == (H-1, W-1):
            break
        
        # horse step
        if cnt < K:
            for i in range(8):
                cx = x
                cy = y

                if i < 4:
                    cx += d1[i]
                    cy += d2[i]
                else:
                    cx += d2[i-4]
                    cy += d1[i-4]

                if 0 <= cx < H and 0 <= cy < W and arr[cx][cy] == 0 and check[cnt+1][cx][cy] == INF:
                    check[cnt+1][cx][cy] = check[cnt][x][y] + 1
                    q.append((cx, cy, cnt+1))

        # monkey step
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < H and 0 <= cy < W and arr[cx][cy] == 0 and check[cnt][cx][cy] == INF:
                check[cnt][cx][cy] = check[cnt][x][y] + 1
                q.append((cx, cy, cnt))


bfs()

for i in range(K+1):
    answer = min(answer, check[i][H-1][W-1])

if answer == INF:
    print(-1)
else:
    print(answer)
