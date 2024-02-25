from sys import stdin

N = int(input())
paper = [list(map(int, stdin.readline().split())) for _ in range(N)]
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

def recur(row, col, size):
    global minus_cnt, zero_cnt, plus_cnt
    comp = paper[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if (comp != paper[i][j]):
                size //= 3
                recur(row, col, size)
                recur(row, col + size, size)
                recur(row, col + (size * 2), size)
                recur(row + size, col, size)
                recur(row + size, col + size, size)
                recur(row + size, col + (size * 2), size)
                recur(row + (size * 2), col, size)
                recur(row + (size * 2), col + size, size)
                recur(row + (size * 2), col + (size * 2), size)
                return

    if comp == -1:
        minus_cnt += 1
    elif comp == 0:
        zero_cnt += 1
    elif comp == 1:
        plus_cnt += 1
 
recur(0, 0, N)
print(minus_cnt)
print(zero_cnt)
print(plus_cnt)