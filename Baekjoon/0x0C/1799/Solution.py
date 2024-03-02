from sys import stdin, setrecursionlimit
from copy import deepcopy

setrecursionlimit(10 ** 6)

N = int(input())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
isused1 = [False] * (N * 2)     # 대각선1 사용 여부
isused2 = [False] * (N * 2)     # 대각선2 사용 여부
max_count1 = 0
max_count2 = 0

def func(x, y, board, color):
    global max_count1, max_count2

    # 이차원 배열의 마지막 행, 열에 도달한 경우
    if (x == N-1 and y == N):
        count = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 2:
                    count += 1
        
        if(color == 0):
            max_count1 = max(max_count1, count)
        else:
            max_count2 = max(max_count2, count)
        return
    
    if y == N:
        func(x + 1, 0, board, color)
        return

    # 비숍을 놓을 수 있는 경우
    if board[x][y] == 1 and not isused1[x-y+(N-1)] and not isused2[x+y]:
        # 비숍을 놓는다
        board[x][y] = 2
        isused1[x-y+(N-1)] = True
        isused2[x+y] = True
        func(x, y + 1, board, color)
        # 비숍을 놓지 않는다
        board[x][y] = 1
        isused1[x-y+(N-1)] = False
        isused2[x+y] = False
        func(x, y + 1, board, color)
    else:
        func(x, y + 1, board, color)

# color_board 별로 비숍을 놓을 수 있는 위치를 설정한다
def get_color_board(color):
    board = deepcopy(graph)

    for i in range(N):
        for j in range(N):
            if ((i + j) % 2 == color):
                board[i][j] = 0
    
    return board

# 다음과 같이 w, b 보드로 분리. w의 비숍과 b의 비숍을 서로 영향을 주지 않음. (대각선에 위치할 수 없음)
# wbwb
# bwbw
# wbwb
# bwbw
white_board = get_color_board(0)
black_board = get_color_board(1)

func(0, 0, white_board, 0)
func(0, 0, black_board, 1)
print(max_count1 + max_count2)
