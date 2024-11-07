from collections import deque
from sys import stdin

N = int(input())
K = int(input())

apple = [[False] * N for _ in range(N)]
snake = deque()
rotate = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 1
cnt = 0

for _ in range(K):
    x, y = map(int, stdin.readline().split())
    apple[x-1][y-1] = True

L = int(input())
for _ in range(L):
    X, C = stdin.readline().split()
    rotate.append((X, C))

def in_range(cx, cy):
    if 0 <= cx < N and 0 <= cy < N:
        return True
    return False

def touch_tail(cx, cy):
    if (cx, cy) in snake:
        return True
    return False

def set_dir(r):
    global dir

    if r == 'D':
        dir = (dir - 1 + 4)  % 4
    else:
        dir = (dir + 1)  % 4
        

snake.append((0, 0))
while snake:
    x, y = snake[0]
    cnt += 1

    cx = x + dx[dir]
    cy = y + dy[dir]
    if (not in_range(cx, cy)) or (touch_tail(cx, cy)):
        break

    if apple[cx][cy]:
        apple[cx][cy] = False
    else:
        snake.pop()
    
    snake.appendleft((cx, cy))
    
    
    if rotate and (cnt == int(rotate[0][0])):
        _, r = rotate.popleft()
        set_dir(r)

print(cnt)
