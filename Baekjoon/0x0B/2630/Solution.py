from sys import stdin

N = int(input())
white_cnt, blue_cnt = 0, 0

papers = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    papers.append(row)

def dc(row, col, n):
    global white_cnt, blue_cnt
    comp = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != comp:
                # 다음 탐색
                next_n = n // 2
                dc(row, col, next_n)
                dc(row, col + next_n, next_n)
                dc(row + next_n, col, next_n)
                dc(row + next_n, col + next_n, next_n)
                return
            
    if comp == 0:
        white_cnt += 1
    elif comp == 1:
        blue_cnt += 1

dc(0, 0, N)
print(white_cnt, blue_cnt, sep="\n")
