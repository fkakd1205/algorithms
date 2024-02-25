from sys import stdin

N = int(input())
paper = [list(map(int, stdin.readline().split())) for _ in range(N)]
w_cnt, b_cnt = 0, 0

def recur(row, col, size):
    global w_cnt, b_cnt
    comp = paper[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if (comp != paper[i][j]):
                size //= 2
                recur(row, col, size)
                recur(row, col + size, size)
                recur(row + size, col, size)
                recur(row + size, col + size, size)
                return

    if comp == 0:
        w_cnt += 1
    elif comp == 1:
        b_cnt += 1

recur(0, 0, N)
print(w_cnt)
print(b_cnt)
