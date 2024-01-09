from sys import stdin
from collections import deque

M, N, H = map(int, input().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N * H)]
q = deque()
count = 0

# 오 아 왼 위 N앞 N뒤
dx = [0, 1, 0, -1, N, N * -1]
dy = [1, 0, -1, 0, 0, 0]

for i in range(N * H):
    for j in range(M):
        if(graph[i][j] == 1):
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(6):
            cx = x + dx[i]
            cy = y + dy[i]
            # 높이 경계 주의
            # (x % N) == 0인 경우 위로 퍼지지 않도록, (x % N) == N - 1인 경우 아래로 퍼지지 않도록 제한
            if(x % N == 0) and (cx % N == (N-1)) or (x % N == (N-1) and (cx % N == 0)):
                continue
            if (0 <= cx < N * H) and (0 <= cy < M) and (graph[cx][cy] == 0):
                graph[cx][cy] = graph[x][y] + 1
                q.append([cx, cy])

bfs()

for i in range(N*H):
    for j in range(M):
        if(graph[i][j] == 0):
            print(-1)
            exit()

        count = max(count, graph[i][j])

# 처음 시작일 빼기
print(count-1)
