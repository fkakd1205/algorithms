from collections import deque

arr = []
row = 0
col = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if 0 <= cx < row and 0 <= cy < col:
                if arr[cx][cy] == 1:
                    arr[cx][cy] += arr[x][y]
                    q.append((cx, cy))

def solution(maps):
    global arr, row, col
    arr = maps
    row = len(maps)
    col = len(maps[0])
    answer = 0
    
    bfs()
    answer = arr[row-1][col-1] if arr[row-1][col-1] != 1 else -1
    return answer

n = int(input())
m = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
print(solution(maps))
