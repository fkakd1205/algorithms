from sys import stdin
from collections import deque

N = int(input())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = 0
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < N):
                if(arr[cx][cy] == 1):
                    arr[cx][cy] = 0
                    q.append((cx, cy))

    return cnt

result = []
count = 0
for i in range(N):
    for j in range(N):
        if(arr[i][j] == 1):
            count += 1
            result.append(bfs(i, j))

print(count)
print(*sorted(result), sep="\n")