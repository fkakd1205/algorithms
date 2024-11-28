from sys import stdin
from collections import deque

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

INF = int(1e5)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

shark_size = 2
feed_count = 0
shark_x, shark_y = -1, -1
answer = 0

def bfs(i, j):
    q = deque()
    q.append((i, j))
    check = [[-1] * N for _ in range(N)]
    check[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < N and check[cx][cy] == -1 and arr[cx][cy] <= shark_size:
                q.append((cx, cy))
                check[cx][cy] = check[x][y] + 1
    
    return check

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark_x, shark_y = i, j
            arr[i][j] = 0

while True:
    checked = bfs(shark_x, shark_y)
    mn_dis = INF

    # 가장 가까운 먹이 확인
    for i in range(N):
        for j in range(N):
            if checked[i][j] != -1 and 0 < arr[i][j] < shark_size:
                if checked[i][j] < mn_dis:
                    shark_x, shark_y = i, j
                    mn_dis = checked[i][j]

    if mn_dis == INF: break
    arr[shark_x][shark_y] = 0
    answer += mn_dis
    feed_count += 1

    # 먹이를 충분히 섭취했다면, 상어 크기 +1
    if shark_size == feed_count:
        feed_count = 0
        shark_size += 1

print(answer)
