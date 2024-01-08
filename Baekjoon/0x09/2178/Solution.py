from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# 오 아 왼 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (0 <= cx < N) and (0 <= cy < M) and (graph[cx][cy] == 1):
                q.append([cx, cy])
                graph[cx][cy] = graph[x][y] + 1     # 방문 횟수 누적

    return graph[N-1][M-1]

print(bfs(0, 0))
