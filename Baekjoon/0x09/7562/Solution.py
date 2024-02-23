from sys import stdin
from collections import deque

T = int(input())
# x, y가 -2, -1, 1, 2씩만 이동한다
d = [-2, -1, 1, 2]

def bfs(x, y, target_x, target_y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if(target_x == x and target_y == y):
            print(arr[x][y] - 1)
            break

        for i in d:
            for j in d:
                # i와 j의 절댓값이 같은 경우의 이동은 하지 않는다
                if abs(i) != abs(j):
                    cx = i + x
                    cy = j + y
                    if (0 <= cx < l and 0 <= cy < l):
                        if(arr[cx][cy] == 0):
                            q.append((cx, cy))
                            arr[cx][cy] = arr[x][y] + 1

for _ in range(T):
    l = int(stdin.readline().rstrip())
    arr = [[0] * l for _ in range(l)]
    x,  y = map(int, stdin.readline().split())
    target_x, target_y = map(int, stdin.readline().split())
    
    arr[x][y] = 1
    bfs(x, y, target_x, target_y)
