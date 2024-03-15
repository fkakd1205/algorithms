from sys import stdin
from collections import deque

N = int(input())
board = [[0] * (N+1) for _ in range(N+1)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

K = int(input())
for _ in range(K):
    x, y = map(int, stdin.readline().split())
    board[x][y] = 2

L = int(input())
change_d = deque()
for _ in range(L):
    time, d = map(str, stdin.readline().split())
    change_d.append((time, d))

def bfs(x, y, dir):
    global cnt, board
    q = deque()
    q.append((x, y, dir))
    board[x][y] = 1

    while q:
        x, y, dir = q[0]

        # 방향 변경
        if (change_d and (cnt == int(change_d[0][0]))):
            _, d = change_d.popleft()
            dir = (dir + 1) if d == 'D' else (dir + 3)
            dir %= 4
            
        cx = x + dx[dir]
        cy = y + dy[dir]
        cnt += 1
        if (0 < cx < N+1 and 0 < cy < N+1 and board[cx][cy] != 1):
            # 사과가 놓여져있다면 몸길이 그대로
            if board[cx][cy] == 2:
                board[cx][cy] = 1
                q.appendleft((cx, cy, dir))
            else:
                board[cx][cy] = 1
                q.appendleft((cx, cy, dir))
                # 빈칸이라면 마지막 꼬리 제거
                last_x, last_y, _ = q.pop()
                board[last_x][last_y] = 0            
        else:
            break

bfs(1, 1, 1)
print(cnt)
