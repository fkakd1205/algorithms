from sys import stdin
from collections import deque
from copy import deepcopy

R = 12
C = 6
graph = [list(map(str, stdin.readline().rstrip())) for _ in range(R)]
graph2 = []
visited = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global visited, graph2

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    graph2 = deepcopy(graph)
    graph2[x][y] = '.'
    is_puyo = False
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1

        if (not is_puyo and cnt >= 4):
            is_puyo = True
        
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < R and 0 <= cy < C):
                if (not visited[cx][cy] and graph[x][y] == graph[cx][cy] and graph2[cx][cy] != '.'):
                    visited[cx][cy] = True
                    q.append((cx, cy))
                    graph2[cx][cy] = '.'

    return is_puyo

def move_by_gravity():
    global graph

    for y in range(C):
        temp = ['.'] * R
        idx = 0
        for x in range(R):
            if graph[R-1-x][y] == '.': continue
            temp[idx] = graph[R-1-x][y]
            idx += 1
        for x in range(R):
            graph[R-1-x][y] = temp[x]

puyo_cnt = 0
while (True):
    is_changed = False
    visited = [[False] * C for _ in range(R)]
    
    # 1. 상하좌우 4개 이상으로 연결된 색상을 제거. '.'로 바꿔준다.
    for i in range(R):
        for j in range(C):
            if graph[i][j] != '.' and not visited[i][j]:
                is_puyo = bfs(i, j)
                if is_puyo:
                    graph = deepcopy(graph2)
                    is_changed = True

    # 2. '.'으로 바뀐 뿌요가 있다면 중력의 영향을 받아 아래로 떨어진다.
    if is_changed:
        puyo_cnt += 1
        move_by_gravity()
    else:
        print(puyo_cnt)
        break
