from sys import stdin
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, L, R = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
answer = 0 

def in_range(x, y, cx, cy):
    if not (0 <= cx < N and 0 <= cy < N):
        return False
    if check[cx][cy] != 0:
        return False
    if not (L <= abs(A[cx][cy] - A[x][y]) <= R):
        return False
    return True

def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    sum = A[x][y]
    check[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if in_range(x, y, cx, cy):
                check[cx][cy] = 1
                q.append((cx, cy))
                cnt += 1
                sum += A[cx][cy]

    return cnt, sum

def update_population(cnt, sum):
    avg = sum // cnt
    for i in range(N):
        for j in range(N):
            if check[i][j] == 1:
                A[i][j] = avg
                check[i][j] = 2

while True:
    check = [[0] * N for _ in range(N)]
    update_cnt = 0

    for i in range(N):
        for j in range(N):
            if check[i][j] == 0:
                c, s = bfs(i, j)
                if c > 1:
                    update_population(c, s)
                    update_cnt += 1
                else:
                    check[i][j] = 2

    if update_cnt == 0:
        break
    answer += 1

print(answer)
