from sys import stdin
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
H, W, x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
checked = [[-1] * M for _ in range(N)]
walls = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            walls.append((i, j))

q = deque()
q.append((x1, y1))
checked[x1][y1] = 0

def check_range(cx, cy):
    if not (0 <= cx < (N - H + 1) and 0 <= cy < (M - W + 1)):
        return False
    
    return True

# 해당 범위내에 벽이 존재하는지
def moveable(cx, cy):
    flag = True

    for (w_x, w_y) in walls:
        if (cx <= w_x < cx + H) and (cy <= w_y < cy + W):
            flag = False
            break

    return flag

while q:
    x, y = q.popleft()
    
    if (x, y) == (x2, y2):
        break

    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if check_range(cx, cy) and moveable(cx, cy) and not board[cx][cy] and checked[cx][cy] == -1:
            checked[cx][cy] = checked[x][y] + 1
            q.append((cx, cy))

print(checked[x2][y2])
