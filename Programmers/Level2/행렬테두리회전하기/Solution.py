R = 0
C = 0
answer = []
INF = int(1e6)

def rotate(arr, x1, y1, x2, y2):
    new_arr = [[0] * C for _ in range(R)]
    min_value = INF

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if x == x1:
                if y == y2:
                    new_arr[x+1][y] = arr[x][y]
                else:
                    new_arr[x][y+1] = arr[x][y]
            elif x == x2:
                if y == y1:
                    new_arr[x-1][y] = arr[x][y]
                else:
                    new_arr[x][y-1] = arr[x][y]
            else:
                if y == y1: # 위로
                    new_arr[x-1][y] = arr[x][y]
                elif y == y2:   # 아래로
                    new_arr[x+1][y] = arr[x][y]

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if new_arr[x][y] != 0:
                arr[x][y] = new_arr[x][y]
                min_value = min(min_value, new_arr[x][y])

    answer.append(min_value)

def solution(rows, columns, queries):
    global R, C
    R = rows + 1
    C = columns + 1
    arr = [[0] * (C) for _ in range(R)]
    
    num = 1
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0: continue
            arr[i][j] = num
            num += 1
    
    for x1, y1, x2, y2 in queries:
        rotate(arr, x1, y1, x2, y2)
    
    return answer

n = int(input().rstrip())
rows = int(input())
columns = int(input())
queries = [list(map(int, input().split())) for _ in range(n)]
print(solution(rows, columns, queries))
