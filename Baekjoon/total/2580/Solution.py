from sys import stdin

N = 9
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
zero_points = []
is_used = [[False] * (N+1) for _ in range(N)]
is_solved = False

# 현재 row에 num이 있으면 pass
def zero_in_row(x, num):
    for y in range(N):
        if arr[x][y] == num:
            return True
    return False

# 현재 col에 num이 있으면 pass
def zero_in_col(y, num):
    for x in range(N):
        if arr[x][y] == num:
            return True
    return False

# 현재 box에 num이 있으면 pass
def zero_in_box(x, y, num):
    x = 3 * (x // 3)
    y = 3 * (y // 3)
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if arr[i][j] == num:
                return True
    return False

# 백트래킹
def recur(cur):
    global is_solved
    if is_solved:
        return
    
    if cur == len(zero_points):
        for line in arr:
            print(*line)
        is_solved = True
        return
    
    x, y = zero_points[cur]
    # 1 ~ 10까지 가능한 num을 찾는다
    for num in range(1, 10):
        if zero_in_row(x, num) or zero_in_col(y, num) or zero_in_box(x, y, num):
            continue
        if not is_used[x][num]:
            is_used[x][num] = True
            arr[x][y] = num
            recur(cur + 1)
            arr[x][y] = 0
            is_used[x][num] = False

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            zero_points.append((i, j))
            
recur(0)
