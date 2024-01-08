from sys import stdin
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
q = deque()
count = 0

# 오 아 왼 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if (graph[i][j] == 1):
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (0 <= cx < N) and (0 <= cy < M) and (graph[cx][cy] == 0):
                q.append([cx, cy])
                graph[cx][cy] = graph[x][y] + 1
            
bfs()

for i in range(N):
    for j in range(M):
        if (graph[i][j] == 0):
            print(-1)
            exit()
        
        count = max(count, graph[i][j])

# 처음 시작일을 빼준다
print(count-1)
