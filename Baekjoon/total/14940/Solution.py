from sys import stdin
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
check = [[-1] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            q.append((i, j))
            check[i][j] = 0
        elif board[i][j] == 0:
            check[i][j] = 0

while q:
    x, y = q.popleft()
    
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < n and 0 <= cy < m and check[cx][cy] == -1:
            check[cx][cy] = check[x][y] + 1
            q.append((cx, cy))
        
for i in range(n):
    print(*check[i])