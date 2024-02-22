from sys import stdin
from collections import deque

R, C = map(int, input().split())
arr = [list(map(str, stdin.readline().rstrip())) for _ in range(R)]
j_graph = [[0] * C for _ in range(R)]
f_graph = [[0] * C for _ in range(R)]
j_q = deque()
f_q = deque()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 1. 지훈이와 불에 대한 graph를 분리. 지훈이 위치와 불의 위치를 큐에 넣는다
for i in range(R):
    for j in range(C):
        if (arr[i][j] == '.'):
            j_graph[i][j] = -1
            f_graph[i][j] = -1
        elif (arr[i][j] == 'J'):
            j_graph[i][j] = 1
            j_q.append((i, j))
        elif (arr[i][j] == 'F'):
            f_graph[i][j] = 1
            f_q.append((i, j))

def f_bfs():
    while(f_q):
        x, y = f_q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < R and 0 <= cy < C):
                # 불이 지나갈 수 있는 경우
                if (f_graph[cx][cy] == -1):
                    f_graph[cx][cy] = f_graph[x][y] + 1
                    f_q.append((cx, cy))

def j_bfs():
    while(j_q):
        x, y = j_q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < R and 0 <= cy < C):
                # 지훈이가 아직 방문하지 않은 곳
                # 불이 지나가지 않았거나(지훈이를 지나치지 못하므로) 불보다 지훈이가 더 빨리 이동한 경우
                if (j_graph[cx][cy] == -1 and (f_graph[cx][cy] == -1 or j_graph[x][y] + 1 < f_graph[cx][cy])):
                        j_graph[cx][cy] = j_graph[x][y] + 1
                        j_q.append((cx, cy))
            else:   # R이나 C의 범위를 벗어났다는 것은 탈출을 성공했다는 것임
                return j_graph[x][y]
    
    return "IMPOSSIBLE"

# 2. 먼저 불에 대해 bfs 진행. 이동시간을 누적
# 3. 지훈이에 대해 bfs 진행. 불의 이동시간과 비교한다
f_bfs()
print(j_bfs())
