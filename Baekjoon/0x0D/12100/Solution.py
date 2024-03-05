from sys import stdin
from copy import deepcopy

N = int(input())
board1 = [list(map(int, stdin.readline().split())) for _ in range(N)]
board2 = []

def rotate():
    temp = deepcopy(board2)

    for i in range(N):
        for j in range(N):
            board2[j][N-1-i] = temp[i][j]

def tilted(dir):
    while (dir > 0):
        dir -= 1
        rotate()
    
    # 회전을 해줬으니, 한 방향에 대한 이동결과를 구하면 됨
    for i in range(N):
        tilted = [0] * N    # 이동시킨 결과
        idx = 0
        for j in range(N):
            if (board2[i][j] == 0): continue
            if (tilted[idx] == 0):
                tilted[idx] = board2[i][j]
            elif (tilted[idx] == board2[i][j]):
                tilted[idx] *= 2
                idx += 1
            else:
                idx += 1
                tilted[idx] = board2[i][j]

        for j in range(N):
            board2[i][j] = tilted[j]

max_value = 0
# 5번을 위, 오, 아, 왼으로 독립적으로 회전시킨다. (4^5)
for k in range(4 ** 5):
    case = k
    board2= deepcopy(board1)

    for i in range(5):
        dir = case % 4
        case //= 4
        tilted(dir)

    for i in range(N):
        for j in range(N):
            max_value = max(max_value, board2[i][j])

print(max_value)
