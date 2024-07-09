from sys import stdin
from collections import deque

INF = int(2e9)
R, C = map(int, input().split())
miro = [list(stdin.readline().rstrip()) for _ in range(R)]
jihoon_m = [[INF] * C for _ in range(R)]
fire_m = [[INF] * C for _ in range(R)]
jihoon_q = deque()
fire_q = deque()
answer = INF

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(map, queue):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if 0 <= cx < R and 0 <= cy < C:
                if map[cx][cy] == INF and miro[cx][cy] == '.':
                    map[cx][cy] = map[x][y] + 1
                    queue.append((cx, cy))

for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            jihoon_m[i][j] = 1
            jihoon_q.append((i, j))
        elif miro[i][j] == 'F':
            fire_m[i][j] = 1
            fire_q.append((i, j))

bfs(jihoon_m, jihoon_q)
bfs(fire_m, fire_q)

for i in range(R):
    for j in range(C):
        if i == 0 or i == R-1 or j == 0 or j == C-1:
            if miro[i][j] == '.' and jihoon_m[i][j] != INF and jihoon_m[i][j] < fire_m[i][j]:
                answer = min(answer, jihoon_m[i][j])
            elif miro[i][j] == 'J':
                answer = jihoon_m[i][j]

if answer == INF:
    print("IMPOSSIBLE")
else:
    print(answer)
