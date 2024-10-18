size = 9
arr = [list(map(int, input().split())) for _ in range(size)]
zero_points = []
is_solved = False

def duplicated_in_line(x, y, num):
    for cx in range(size):
        if arr[cx][y] == num:
            return True

    for cy in range(size):
        if arr[x][cy] == num:
            return True

    return False

def duplicated_in_box(x, y, num):
    x = 3 * (x // 3)
    y = 3 * (y // 3)
    for cx in range(x, x+3):
        for cy in range(y, y+3):
            if arr[cx][cy] == num:
                return True
    return False

def brute_force(cur):
    global is_solved

    if is_solved:
        return
    
    if cur == len(zero_points):
        for i in range(size):
            print(" ".join(map(str, arr[i])))
        is_solved = True
        return
    
    x, y = zero_points[cur]
    for num in range(1, 10):
        if duplicated_in_line(x, y, num): continue
        if duplicated_in_box(x, y, num): continue
        arr[x][y] = num
        brute_force(cur+1)
        arr[x][y] = 0

for i in range(size):
    for j in range(size):
        if arr[i][j] == 0:
            zero_points.append((i, j))

brute_force(0)
