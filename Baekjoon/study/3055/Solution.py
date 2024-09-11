from sys import stdin
from collections import deque

R, C = map(int, input().split())
map = [list(stdin.readline()) for _ in range(R)]
check1 = [[0] * C for _ in range(R)]
check2 = [[0] * C for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
target = (-1, -1)

def check_water(cx, cy):
    if not (0 <= cx < R and 0 <= cy < C):
        return False
    if check1[cx][cy] != 0:
        return False
    if map[cx][cy] == 'X' or map[cx][cy] == 'D':
        return False
    return True

def check_s(x, y, cx, cy):
    if not (0 <= cx < R and 0 <= cy < C):
        return False
    if map[cx][cy] == 'X':
        return False
    if check2[cx][cy] != 0:
        return False
    if check1[cx][cy] != 0 and check1[cx][cy] <= check2[x][y] + 1:
        return False
    return True

def water_bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if check_water(cx, cy):
                check1[cx][cy] = check1[x][y] + 1
                q.append((cx, cy))

def s_bfs():
    while q:
        x, y = q.popleft()
        
        if target == (x, y):
            break

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            
            if check_s(x, y, cx, cy):
                check2[cx][cy] = check2[x][y] + 1
                q.append((cx, cy))

q = deque()
for i in range(R):
    for j in range(C):
        if map[i][j] == '*':
            q.append((i, j))
            check1[i][j] = 1

water_bfs()

q = deque()
for i in range(R):
    for j in range(C):
        if map[i][j] == 'S':
            q.append((i, j))
            check2[i][j] = 1
        elif map[i][j] == 'D':
            target = (i, j)

s_bfs()

if check2[target[0]][target[1]] == 0:
    print("KAKTUS")
else:
    print(check2[target[0]][target[1]] - 1)
