from sys import stdin
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

def bfs():
    global answer
    q = deque()
    temp = deepcopy(board)
    safe_area = 0

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < M and temp[cx][cy] == 0:
                temp[cx][cy] = 2
                q.append((cx, cy))

    for i in range(N):
        safe_area += temp[i].count(0)

    answer = max(answer, safe_area)

def install_wall(cur):
    if cur == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                install_wall(cur + 1)
                board[i][j] = 0

install_wall(0)
print(answer)
