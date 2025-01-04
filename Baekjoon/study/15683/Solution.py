from sys import stdin
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
cctv = []
answer = N * M

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check_range(cx, cy):
    return 0 <= cx < N and 0 <= cy < M

def check(x, y, dir):
    dir %= 4

    while True:
        x += dx[dir]
        y += dy[dir]
        if not check_range(x, y) or board2[x][y] == 6:
            return
        if board2[x][y] == 0:
            board2[x][y] = 7

# cctv 위치 확인
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append((i, j))

# 4방향 경우의 수 모두 확인
for k in range(4 ** len(cctv)):
    case = k
    board2 = deepcopy(board)

    for x, y in cctv:
        dir = case % 4
        case //= 4

        if board[x][y] == 1:
            check(x, y, dir)
        elif board[x][y] == 2:
            check(x, y, dir)
            check(x, y, dir+2)
        elif board[x][y] == 3:
            check(x, y, dir)
            check(x, y, dir+1)
        elif board[x][y] == 4:
            check(x, y, dir)
            check(x, y, dir+1)
            check(x, y, dir+2)
        elif board[x][y] == 5:
            check(x, y, dir)
            check(x, y, dir+1)
            check(x, y, dir+2)            
            check(x, y, dir+3)

    # 사각지대 확인
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if board2[i][j] == 0:
                zero_cnt += 1
    
    answer = min(answer, zero_cnt)

print(answer)
