# from sys import stdin
# from collections import deque

# n, m = map(int, input().split())
# graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
# visited = [([False] * m) for _ in range(n)]

# # 오 아 왼 위
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# 테스트 실패 입력값
# 1 1
# 1
# 출력
# 1
# 0
# why ? cx, cy의 범위가 넘어가 현재 색칠된 범위를 구할 수 없다

# def bfs(x, y):
#     q = deque()
#     q.append([x, y])
#     width = 0

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             cx = x + dx[i]
#             cy = y + dy[i]
#             if (0 <= cx < n) and (0 <= cy < m):
#                 if (graph[cx][cy] == 1) and (visited[cx][cy] == False):
#                     width += 1
#                     visited[cx][cy] = True
#                     q.append([cx, cy])
#     return width

# count = 0
# max_width = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치가 그림이고, 방문하지 않았다면
#         if (graph[i][j] == 1) and (visited[i][j] == False):
#             count += 1
#             max_width = max(bfs(i, j), max_width)

# print(count)
# print(max_width)

from sys import stdin
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [([False] * m) for _ in range(n)]

# 오 아 왼 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    width = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (0 <= cx < n) and (0 <= cy < m):
                if (graph[cx][cy] == 1) and (visited[cx][cy] == False):
                    width += 1
                    visited[cx][cy] = True
                    q.append([cx, cy])
    return width

count = 0
max_width = 0
for i in range(n):
    for j in range(m):
        # 현재 위치가 그림이고, 방문하지 않았다면
        if (graph[i][j] == 1) and (visited[i][j] == False):
            visited[i][j] = True
            count += 1
            max_width = max(bfs(i, j), max_width)

print(count)
print(max_width)
