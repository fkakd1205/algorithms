from sys import stdin
from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def change_range(x, y, cx, cy):
    if not (0 <= cx < N and 0 <= cy < N):
        return False
    if not (L <= abs(arr[x][y] - arr[cx][cy]) <= R):
        return False
    if visited[cx][cy] != 0:
        return False
    return True

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    sum = arr[x][y]
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if change_range(x, y, cx, cy):
                visited[cx][cy] = 1
                q.append((cx, cy))
                sum += arr[cx][cy]
                cnt += 1

    return sum, cnt

def update_people(people_cnt):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                arr[i][j] = people_cnt
                visited[i][j] = 2

answer = 0
while(True):
    # 0 : 방문 X
    # 1 : 방문 O, 인구이동 전
    # 2 : 방문 O, 인구이동 후
    visited = [[0] * N for _ in range(N)]
    is_changed = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0: continue
            sum, cnt = bfs(i, j)
            # 인구이동이 필요하다면 update
            if cnt > 1:
                update_people(sum // cnt)
                is_changed = True
            else:
                visited[i][j] = 2

    if is_changed:
        answer += 1
    else:
        break

print(answer)
