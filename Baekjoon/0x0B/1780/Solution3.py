N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

def div_papaer(size, x, y):
    global minus_cnt, zero_cnt, plus_cnt
    is_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[x][y] != paper[i][j]:
                is_same = False
                break
        if not is_same: break

    if is_same:
        if paper[x][y] == -1: minus_cnt += 1
        elif paper[x][y] == 0: zero_cnt += 1
        else: plus_cnt += 1
    else:
        new_size = size // 3
        # 9 등분
        for i in range(x, x + size):
            for j in range(y, y + size):
                if i % new_size == 0 and j % new_size == 0:
                    div_papaer(new_size, i, j)

div_papaer(N, 0, 0)
print(minus_cnt, zero_cnt, plus_cnt, sep='\n')