from sys import stdin
from collections import deque

N = int(input())
arr = [list(stdin.readline().rstrip()) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

check = [[0] * N for _ in range(N)]
q = deque()

def bfs(x, y, ck):
    q.append((x, y))
    check[x][y] = ck

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < N\
                and check[cx][cy] != ck and arr[cx][cy] == arr[x][y]:
                check[cx][cy] = ck
                q.append((cx, cy))

answer1 = 0
for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            bfs(i, j, 1)
            answer1 += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

answer2 = 0
for i in range(N):
    for j in range(N):
        if check[i][j] == 1:
            bfs(i, j, 2)
            answer2 += 1

print(answer1, answer2)
