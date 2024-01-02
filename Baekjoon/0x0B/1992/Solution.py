N = int(input())
trees = [list(map(int, input())) for _ in range(N)]
answer = ""

def dc(row, col, n):
    check = trees[row][col]
    global answer

    for i in range(row, row + n):
        for j in range(col, col + n):
            if check != trees[i][j]:
                next_n = n // 2
                answer += "("
                dc(row, col, next_n)    # 왼쪽 위
                dc(row, col + next_n, next_n)   # 오른쪽 위
                dc(row + next_n, col, next_n)   # 왼쪽 아래
                dc(row + next_n, col + next_n, next_n)  # 오른쪽 아래
                answer += ")"
                return
    
    if check == 0:
        answer += "0"
    elif check == 1:
        answer += "1"

dc(0, 0, N)
print(answer)
