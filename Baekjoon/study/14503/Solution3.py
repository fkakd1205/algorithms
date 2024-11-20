from sys import stdin
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, dir):
    q = deque()
    q.append((x, y))
    check[x][y] = True
    
    while q:
        x, y = q.popleft()
        is_moveable = False
        
        for _ in range(4):
            dir = (dir + 3) % 4
            cx = x + dx[dir]
            cy = y + dy[dir]
            if 0 <= cx < N and 0 <= cy < M and board[cx][cy] == 0 and not check[cx][cy]:
                check[cx][cy] = True
                q.append((cx, cy))
                is_moveable = True
                break
        
        # is_moveable이 False이므로 dir이 제자리도 돌아옴
        if not is_moveable:
            cx = x - dx[dir]
            cy = y - dy[dir]
            if board[cx][cy] == 1:
                break
            else:
                q.append((cx, cy))

bfs(r, c, d)
print(sum(map(sum, check)))
