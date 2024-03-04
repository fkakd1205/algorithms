from sys import stdin
from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
cctv =[]
result = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check_range(x, y):
    return 0 <= x < N and 0 <= y < M

def move(x, y, dir):
    dir %= 4
    while(True):
        x += dx[dir]
        y += dy[dir]
        if (not check_range(x, y) or arr2[x][y] == 6):
            return
        if (arr2[x][y] == 0):
            arr2[x][y] = 7

# 1. cctv의 위치와 개수를 구한다.
for i in range(N):
    for j in range(M):
        if (arr[i][j] == 0):
            result += 1 # 사각지대 개수
        if (arr[i][j] != 0 and arr[i][j] != 6):
            cctv.append((i, j)) # cctv 위치

# 2. cctv 개수만큼. 하나씩 회전시킨다. (cctv k개 - k개를 독립적으로 동서남북 회전시켜야 함 => 4^k)
for k in range(4 ** len(cctv)):
    case = k
    arr2 = deepcopy(arr)

    for i in range(len(cctv)):
        dir = case % 4
        case //= 4

        x, y = cctv[i]
        if (arr[x][y] == 1):
            move(x, y, dir)
        elif (arr[x][y] == 2):
            move(x, y, dir)
            move(x, y, dir+2)
        elif (arr[x][y] == 3):
            move(x, y, dir)
            move(x, y, dir+1)
        elif (arr[x][y] == 4):
            move(x, y, dir)
            move(x, y, dir+1)
            move(x, y, dir+2)
        elif (arr[x][y] == 5):
            move(x, y, dir)
            move(x, y, dir+1)
            move(x, y, dir+2)
            move(x, y, dir+3)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr2[i][j] == 0:
                cnt += 1
    result = min(result, cnt)     

print(result)
