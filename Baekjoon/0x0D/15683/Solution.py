from sys import stdin
from copy import deepcopy

N, M = map(int, input().split())
board1 = [list(map(int, stdin.readline().split())) for _ in range(N)]
board2 = []
cctv = []
min_zero_cnt = N * M    # cctv가 한개도 없는 경우 0의 최대 개수 (벽 무시)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if(1 <= board1[i][j] <= 5):
            cctv.append([i, j])

def check_range(x, y):
    return 0 <= x < N and 0 <= y < M

def move(x, y, dir):
    dir %= 4
    while(True):
        # 한 방향으로 계속 검사
        x += dx[dir]
        y += dy[dir]
        if(not check_range(x, y) or board2[x][y] == 6): break
        if(board2[x][y] != 0): continue
        board2[x][y] = '#'  # 감시 가능 표시

# 4의 k(cctv개수)승. cctv 개수만큼 하나씩 네방향을 돌려본다
for i in range(4**len(cctv)):
    temp = i    # i = 0, 1, 2, ..., 63
    board2 = deepcopy(board1)   # board2 초기화

    for j in range(len(cctv)):
        dir = temp % 4  # dir을 4진수로 표현하기 위해 (4진수 = 하나의 cctv를 90도씩 돌려봤을 때 나오는 전체 경우의 수)
        temp //= 4
        x = cctv[j][0]
        y = cctv[j][1]
        if(board1[x][y] == 1):
            move(x, y, dir)
        elif(board1[x][y] == 2):
            move(x, y, dir)
            move(x, y, dir+2)
        elif(board1[x][y] == 3):
            move(x, y, dir)
            move(x, y, dir+1)
        elif(board1[x][y] == 4):
            move(x, y, dir)
            move(x, y, dir+1)
            move(x, y, dir+2)
        elif(board1[x][y] == 5):
            move(x, y, dir)
            move(x, y, dir+1)
            move(x, y, dir+2)
            move(x, y, dir+3)
    
    zero_cnt = 0
    for x in range(N):
        for y in range(M):
            if(board2[x][y] == 0):
                zero_cnt += 1
    
    min_zero_cnt = min(min_zero_cnt, zero_cnt)

print(min_zero_cnt)
