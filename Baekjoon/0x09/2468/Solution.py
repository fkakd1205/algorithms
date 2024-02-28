from sys import stdin
from collections import deque

N = int(input())
arr = []
max_height = 0
visited = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < N):
                if (not visited[cx][cy]):
                    visited[cx][cy] = True
                    q.append((cx, cy))

# 가장 큰 
for i in range(N):
    height = list(map(int, stdin.readline().split()))
    max_height = max(max_height, *height)

    arr.append(height)

# 모든 건물의 높이가 1인 경우와 높이가 다 동일한 경우, 잠기지 않는 영역 1 처리
max_area = 1

# 높이 별 visited 표시, visited되지 않은 곳들을 따라 bfs 진행
for h in range(1, max_height):
    visited = [[False] * N for _ in range(N)]

    # h 보다 높이가 같거나 낮은 건물들 표시
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= h:
                visited[i][j] = True

    # h 보다 높이가 높은 건물 bfs 진행
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                bfs(i, j)

    max_area = max(max_area, cnt)

print(max_area)