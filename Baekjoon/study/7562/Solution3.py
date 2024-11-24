from sys import stdin
from collections import deque

T = int(input())
d1 = [-2, 2, 2, -2]
d2 = [1, 1, -1, -1]

for _ in range(T):
    I = int(stdin.readline().rstrip())
    start_x, start_y = map(int, stdin.readline().split())
    target_x, target_y = map(int, stdin.readline().split())
    visited = [[-1] * I for _ in range(I)]

    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        if (x, y) == (target_x, target_y):
            print(visited[x][y])
            break

        for i in range(8):
            cx, cy = x, y
            if i < 4:
                cx += d1[i]
                cy += d2[i]
            else:
                cx += d2[i-4]
                cy += d1[i-4]

            if 0 <= cx < I and 0 <= cy < I and visited[cx][cy] == -1:
                q.append((cx, cy))
                visited[cx][cy] = visited[x][y] + 1
