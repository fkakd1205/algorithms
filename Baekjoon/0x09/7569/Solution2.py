from sys import stdin
from collections import deque

M, N, H = map(int, input().split())
# 3차원 배열 사용
graph = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]
q = deque()
count = 0

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if(graph[i][j][k] == 1):
                q.append([i, j, k])

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            cx = x + dx[i]
            cy = y + dy[i]
            cz = z + dz[i]
            if (0 <= cx < N) and (0 <= cy < M) and (0 <= cz < H) and (graph[cz][cx][cy] == 0):
                graph[cz][cx][cy] = graph[z][x][y] + 1
                q.append([cz, cx, cy])

bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if(graph[i][j][k] == 0):
                print(-1)
                exit()

            count = max(count, graph[i][j][k])

# 처음 시작일 빼기
print(count-1)
