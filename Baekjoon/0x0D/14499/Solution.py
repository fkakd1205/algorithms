from sys import stdin
from copy import deepcopy

N, M, x, y, K = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dir = list(map(int, stdin.readline().split()))
dice = [[0] * 3 for _ in range(4)]

def update_pos(d):
    new_x, new_y = x, y

    if(d == 1):
        new_y = y + 1
    elif(d == 2):
        new_y = y - 1
    elif(d == 3):
        new_x = x - 1
    else:
        new_x = x + 1
    
    if(0 <= new_x < N and 0 <= new_y < M):
        return new_x, new_y
    else:
        return x, y

def update_dice(d):
    global dice
    dice2 = deepcopy(dice)

    # 동
    if(d == 1):
        dice[1][1] = dice2[1][0]
        dice[1][2] = dice2[1][1]   
        dice[3][1] = dice2[1][2]   
        dice[1][0] = dice2[3][1]   
    # 서
    elif(d == 2):
        dice[1][1] = dice2[1][2]
        dice[1][0] = dice2[1][1]   
        dice[3][1] = dice2[1][0]
        dice[1][2] = dice2[3][1]
    # 북
    elif(d == 3):
        for x in range(4):
            dice[x][1] = dice2[(x+1) % 4][1]
    # 남
    else:
        for x in range(4):
            dice[(x+1) % 4][1] = dice2[x][1]
        

for d in dir:
    # 1. 주사위 위치 변경
    cx, cy = update_pos(d)
    if(cx == x and cy == y):
        continue

    x, y = cx, cy
    # 2. 주사위 세팅
    update_dice(d)
    
    # 3. board 숫자에 따른 값 세팅
    if(board[x][y] == 0):
        board[x][y] = dice[3][1]
    else:
        dice[3][1] = board[x][y]
        board[x][y] = 0

    print(dice[1][1])
