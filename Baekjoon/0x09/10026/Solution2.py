from sys import stdin
from collections import deque

N = int(input())
arr = [list(stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < N):
                if(not visited[cx][cy] and arr[x][y] == arr[cx][cy]):
                    q.append((cx, cy))
                    visited[cx][cy] = True
        
count = 0
for i in range(N):
    for j in range(N):
        if(not visited[i][j]):
            bfs(i, j)
            count += 1

print(count, end=" ")

# 적록색약의 시야를 보기 위해 G -> R로 변경
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

# 방문 여부 초기화
visited = [[False] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if(not visited[i][j]):
            bfs(i, j)
            count += 1

print(count)