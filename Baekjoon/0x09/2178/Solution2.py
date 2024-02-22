from sys import stdin
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < M):
                if(not visited[cx][cy] and arr[cx][cy] == 1):
                    q.append((cx, cy))
                    # 이동 횟수 누적
                    arr[cx][cy] = arr[x][y] + 1

bfs(0, 0)
print(arr[N-1][M-1])
