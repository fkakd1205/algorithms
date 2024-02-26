from sys import stdin
from collections import deque

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = 1
    cnt = 0

    while(q):
        x, y = q.popleft()
        cnt += 1

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if(0 <= cx < M and 0 <= cy < N):
                if(arr[cx][cy] == 0):
                    arr[cx][cy] = 1
                    q.append((cx, cy))

    return cnt

for _ in range(K):
    c1, r1, c2, r2 = map(int, stdin.readline().split())

    for i in range(r1, r2):
        for j in range(c1, c2):
            arr[i][j] = 1

result = []
count = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            count += 1
            result.append(bfs(i, j))

print(count)
print(*sorted(result), sep=" ")