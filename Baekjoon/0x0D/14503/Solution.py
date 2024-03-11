from sys import stdin
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]
    
def dfs(x, y, dir):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        is_completed = True
        
        # 3번 조건 실행. 반시계 방향으로 회전
        for _ in range(4):
            dir = (dir + 3) % 4
            cx = dx[dir] + x
            cy = dy[dir] + y

            if (0 <= cx < N and 0 <= cy < M and visited[cx][cy] == 0):
                q.append((cx, cy))
                visited[cx][cy] = 1
                is_completed = False
                break
        
        # 2번 조건 실행. 후진 이동
        if is_completed:
            cx = x - dx[dir]
            cy = y - dy[dir]
            # 벽 체크
            if visited[cx][cy] != -1:
                q.append((cx, cy))
            else:
                break

# 벽인 경우 visited -1로 초기화
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visited[i][j] = -1

dfs(r, c, d)
sum = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            sum += 1

print(sum)
