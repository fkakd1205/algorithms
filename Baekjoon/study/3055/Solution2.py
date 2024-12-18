from sys import stdin
from collections import deque

R, C = map(int, input().split())
board = [list(stdin.readline().rstrip()) for _ in range(R)]
water_q = deque()
water_check = [[0] * C for _ in range(R)]
go_check = [[0] * C for _ in range(R)]
go_q = deque()
target = (0, 0)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_moveable_water(cx, cy):
    if not (0 <= cx < R and 0 <= cy < C):
         return False
    if not (board[cx][cy] != 'D' and board[cx][cy] != 'X'):
        return False
    if water_check[cx][cy] != 0:
        return False
    return True

def is_moveable_go(x, y, cx, cy):
    if not (0 <= cx < R and 0 <= cy < C):
         return False
    if board[cx][cy] == 'D':
         return True
    if not (board[cx][cy] != '*' and board[cx][cy] != 'X'):
        return False
    if go_check[cx][cy] != 0:
        return False
    if water_check[cx][cy] != 0 and go_check[x][y] + 1 >= water_check[cx][cy]:
        return False
    return True

def water_bfs():
    while water_q:
        x, y = water_q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if is_moveable_water(cx, cy):
                water_check[cx][cy] = water_check[x][y] + 1
                water_q.append((cx, cy))            

def go_bfs():
    while go_q:
        x, y = go_q.popleft()

        if (x, y) == target:
            return True

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if is_moveable_go(x, y, cx, cy):
                go_q.append((cx, cy))
                go_check[cx][cy] = go_check[x][y]+1

    return False

for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            water_q.append((i, j))
            water_check[i][j] = 1
        elif board[i][j] == 'S':
            go_q.append((i, j))
            go_check[i][j] = 1
        elif board[i][j] == 'D':
            target = (i, j)

water_bfs()
if go_bfs():
    print(go_check[target[0]][target[1]]-1)
else:
    print("KAKTUS")
