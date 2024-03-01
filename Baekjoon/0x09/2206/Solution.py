from sys import stdin
from collections import deque

# V1. 틀림
N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
# visited[x][y][0]은 벽을 파괴하지 않은 경로, visited[x][y][1]은 벽을 파괴한 경로
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, break_count):
    q = deque()
    q.append((x, y, break_count))

    while q:
        x, y, break_count = q.popleft()

        if(x == N-1 and y == M-1):
            return visited[x][y][break_count]

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < M):
                # 이동할 수 있는 곳인 경우
                if (arr[cx][cy] == 0 and visited[cx][cy][break_count] == 0):
                    visited[cx][cy][break_count] = visited[x][y][break_count] + 1
                    q.append((cx, cy, break_count))
                # 깰 수 있는 벽인 경우
                elif (arr[cx][cy] == 1 and break_count == 0):
                    visited[cx][cy][break_count + 1] = visited[x][y][break_count] + 1
                    q.append((cx, cy, break_count + 1))

    return -1

visited[0][0][0] = 1

result = bfs(0, 0, 0)
print(result)
