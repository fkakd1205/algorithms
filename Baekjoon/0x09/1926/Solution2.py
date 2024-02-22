from sys import stdin
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [([False] * m) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
color = []  # 색칠된 종이 좌표를 담는 배열

for i in range(n):
    for j in range(m):
        if (arr[i][j]):
            color.append((i, j))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    width = 0

    while(q):
        x, y = q.popleft()
        if (visited[x][y]):
            continue
        visited[x][y] = True
        width += 1
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if(0 <= cx < n and 0 <= cy < m and not visited[cx][cy] and arr[cx][cy] == 1):
                q.append((cx, cy))

    return width

count = 0
max_width = 0
# 그림이 그려진 부분들만 모아서 bfs 탐색
for i in range(len(color)):
    x = color[i][0]
    y = color[i][1]
    if (not visited[x][y]):
        count += 1
        max_width = max(max_width, bfs(x, y))

print(count)
print(max_width)