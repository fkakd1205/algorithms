R = 0
C = 0

# 범위 검사
def check(x, y, board):
    if x + 1 >= R or y + 1 >= C or board[x][y] == '':
        return False
    
    cur = board[x][y]
    if cur == board[x+1][y] and cur == board[x][y+1] and cur == board[x+1][y+1]:
        return True
    
    return False

# 지워진 4블록에 대해 board를 새로 세팅
def change_board(board, board2):
    for j in range(C):
        y_board = [''] * R
        y_idx = R-1
        for i in range(R-1, -1, -1):
            if board2[i][j] == 0:
                y_board[y_idx] = board[i][j]
                y_idx -= 1
        
        for i in range(R-1, -1, -1):
            board[i][j] = y_board[i] 

def solution(m, n, board):
    global R, C
    answer = 0
    R = m
    C = n
    for i in range(R):
        board[i] = list(board[i])

    while True:
        cnt = 0
        board2 = [[0] * n for _ in range(m)]
        for i in range(R-1):
            for j in range(C-1):
                # 4블록
                if check(i, j, board):
                    board2[i][j] = 1
                    board2[i+1][j] = 1
                    board2[i][j+1] = 1
                    board2[i+1][j+1] = 1
        
        for i in range(R):
            cnt += sum(board2[i])
        if cnt == 0:
            break

        answer += cnt
        change_board(board, board2)     # 지워진 4블록에 대해 board를 새로 세팅
    
    return answer

m, n = map(int, input().split())
board = [input() for _ in range(m)]
print(solution(m, n, board))
