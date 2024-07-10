from sys import stdin
from collections import deque

INF = int(1e9)
k = int(input().rstrip())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def fire_bfs():
    while f_queue:
        x, y = f_queue.popleft()
        
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y

            if 0 <= cx < h and 0 <= cy < w\
                and board[cx][cy] == '.' and f_board[cx][cy] == INF:
                f_queue.append((cx, cy))
                f_board[cx][cy] = f_board[x][y] + 1

def sang_bfs():
    answer = INF

    while s_queue:
        x, y = s_queue.popleft()
        
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y

            if 0 <= cx < h and 0 <= cy < w:
                if(board[cx][cy] == '.' and s_board[cx][cy] == INF and s_board[x][y] + 1 < f_board[cx][cy]):
                    s_queue.append((cx, cy))
                    s_board[cx][cy] = s_board[x][y] + 1
            else:
                answer = s_board[x][y]
                break
        
        # 찾는 즉시 탈출
        if answer != INF: break

    return answer


for _ in range(k):
    w, h = map(int, stdin.readline().split())
    board = [list(stdin.readline().rstrip()) for _ in range(h)]

    s_board = [[INF] * w for _ in range(h)]
    f_board = [[INF] * w for _ in range(h)]
    s_queue = deque()
    f_queue = deque()

    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                f_board[i][j] = 1
                f_queue.append((i, j))
            elif board[i][j] == '@':
                s_board[i][j] = 1
                s_queue.append((i, j))

    fire_bfs()
    answer = sang_bfs()

    if answer != INF:
        print(answer)
    else:
        print("IMPOSSIBLE")
