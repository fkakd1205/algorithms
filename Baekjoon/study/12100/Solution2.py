from sys import stdin
from copy import deepcopy

N = int(input())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
board2 = []
answer = 0

def rotate():
    temp = deepcopy(board2)

    for i in range(N):
        for j in range(N):
            board2[j][N-i-1] = temp[i][j]

def check_board(dir):
    # 한 방향으로 미는 경우만 생각하기 위해, 보드 회전
    while dir > 0:
        rotate()
        dir -= 1
    
    # 왼쪽으로 밀기
    for i in range(N):
        temp = [0] * N
        idx = 0
        for j in range(N):
            if board2[i][j] == 0: continue
            if temp[idx] == 0:
                temp[idx] = board2[i][j]
            elif temp[idx] == board2[i][j]:
                temp[idx] *= 2
                idx += 1
            else:
                idx += 1
                temp[idx] = board2[i][j]
        
        for j in range(N):
            board2[i][j] = temp[j]

for k in range(4 ** 5):
    case = k
    board2 = deepcopy(board)

    for i in range(5):
        dir = case % 4
        case //= 4
        check_board(dir)
    
    # 최대 수 계산
    answer = max(answer, max(map(max, board2)))

print(answer)
