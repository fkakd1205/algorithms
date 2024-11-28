from sys import stdin
from collections import deque

INF = int(1e7)
R, C = map(int, input().split())
board = [list(stdin.readline().rstrip()) for _ in range(R)]

f_q = deque()
j_q = deque()

f_check = [[INF] * C for _ in range(R)]
j_check = [[INF] * C for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]
answer = INF

def move_check_for_fire(cx, cy):
    if not (0 <= cx < R and 0 <= cy < C):
        return False
    if board[cx][cy] != '.':
        return False
    if f_check[cx][cy] != INF:
        return False
    return True

def move_check_for_jihun(x, y, cx, cy):
    if not (0 <= cx < R and 0 <= cy < C):
        return False
    if board[cx][cy] != '.':
        return False
    if j_check[cx][cy] != INF:
        return False
    if j_check[x][y] + 1 >= f_check[cx][cy]:
        return False
    return True

def f_bfs():
    while f_q:
        x, y = f_q.popleft()
    
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if move_check_for_fire(cx, cy):
                f_q.append((cx, cy))
                f_check[cx][cy] = f_check[x][y] + 1

def j_bfs():
    while j_q:
        x, y = j_q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if move_check_for_jihun(x, y, cx, cy):
                j_q.append((cx, cy))
                j_check[cx][cy] = j_check[x][y] + 1

for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            j_q.append((i, j))
            j_check[i][j] = 1
        elif board[i][j] == 'F':
            f_q.append((i, j))
            f_check[i][j] = 1

f_bfs()
j_bfs()

for i in range(R):
    for j in range(C):
        if i == 0 or i == R-1:
            if j_check[i][j] != INF:
                answer = min(answer, j_check[i][j])
        elif j == 0 or j == C-1:
            if j_check[i][j] != INF:
                answer = min(answer, j_check[i][j])

if answer == INF:
    print("IMPOSSIBLE")
else:
    print(answer)
