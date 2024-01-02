from sys import stdin

n = int(input())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

papers = []
for _ in range(n):
    row = list(map(int, stdin.readline().split()))
    papers.append(row)

def dc(row, col, n):
    global minus_cnt, zero_cnt, plus_cnt
    comp = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != comp:
                # 다음 탐색 종이
                next_n = n // 3
                dc(row, col, next_n)     # (0, 0)
                dc(row, col + next_n, next_n)    # (0, 3)
                dc(row, col + (2 * next_n), next_n)  # (0, 6)
                dc(row + next_n, col, next_n)    # (3, 0)
                dc(row + next_n, col + next_n, next_n)   # (3, 3)
                dc(row + next_n, col + (2 * next_n), next_n)     # (3, 6)
                dc(row + (2 * next_n), col, next_n)      # (6, 0)
                dc(row + (2 * next_n), col + next_n, next_n)     # (6, 3)
                dc(row + (2 * next_n), col + (2 * next_n), next_n)    # (6, 6)
                return

    if comp == -1:
        minus_cnt += 1
    elif comp == 0:
        zero_cnt += 1
    elif comp == 1:
        plus_cnt += 1

dc(0, 0, n)
print(minus_cnt, zero_cnt, plus_cnt, sep="\n")
