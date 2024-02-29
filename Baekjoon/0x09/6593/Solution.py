from sys import stdin
from collections import deque

dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while(True):
    L, R, C = map(int, input().split())
    arr = []
    q = deque()

    if ((L + R + C) == 0): break

    for _ in range(L):
        arr.append([list(stdin.readline().rstrip()) for _ in range(R)])
        temp = stdin.readline().rstrip()

    for k in range(L):
        for i in range(R):
            for j in range(C):
                if arr[k][i][j] == 'S':
                    q.append((k, i, j))
                    arr[k][i][j] = 0

    minutes = 0
    while(q):
        z, x, y = q.popleft()
        
        for i in range(6):
            cz = dz[i] + z
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cz < L and 0 <= cx < R and 0 <= cy < C):
                if(arr[cz][cx][cy] == '.'):
                    arr[cz][cx][cy] = arr[z][x][y] + 1
                    q.append((cz, cx, cy))
                elif(arr[cz][cx][cy] == 'E'):   # 탈출 성공한다면 minutes 계산하고 큐 clear
                    minutes = arr[z][x][y] + 1
                    q.clear()
                    break
    
    if minutes != 0:
        print("Escaped in %d minute(s)." % minutes)
    else:
        print("Trapped!")
