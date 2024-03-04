from sys import stdin
from copy import deepcopy

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]

def is_attach(x, y, sticker):
    r = len(sticker)
    c = len(sticker[0])

    for i in range(r):
        for j in range(c):
            # 노트북에 스티커를 붙일 수 없다면
            if(sticker[i][j] == 1 and board[x+i][y+j] == 1):
                return False

    # 스티커를 붙일 수 있는 경우
    for i in range(r):
        for j in range(c):
            if(sticker[i][j] == 1):
                board[x+i][y+j] = 1

    return True

def rotate(sticker):
    r = len(sticker)
    c = len(sticker[0])

    temp = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            temp[j][(r-1)-i] = sticker[i][j]
    return temp

for _ in range(K):
    R, C = map(int, stdin.readline().split())
    sticker = [list(map(int, stdin.readline().split())) for _ in range(R)]

    for k in range(4):
        is_attached = False
        # 스티커를 붙일 수 있는 범위만 검사
        # i, j는 스티커를 붙일 수 있는 시작위치
        for i in range(N-R+1):
            for j in range(M-C+1):
                if (is_attach(i, j, sticker)):
                    is_attached = True
                    break
            if is_attached: break
        if is_attached: break
        
        # 90도 회전. R, C 값 변경
        sticker = rotate(sticker)
        R, C = C, R

result = 0
for i in range(N):
    for j in range(M):
        result += board[i][j]

print(result)
