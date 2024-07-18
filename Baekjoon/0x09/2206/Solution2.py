from sys import stdin
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
# visited[x][y][0] 벽 안 부순 경로, visited[x][y][1] 벽 부순 경로
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [0, 1, 0 , -1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, break_cnt = q.popleft()

        if (x == N-1 and y == M-1):
            return visited[x][y][break_cnt]
        
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if 0 <= cx < N and 0 <= cy < M:
                # 다음이 이동할 수 있는 칸이면서 아직 방문하지 않은 경우
                if arr[cx][cy] == 0 and visited[cx][cy][break_cnt] == 0:
                    q.append((cx, cy, break_cnt))
                    visited[cx][cy][break_cnt] = visited[x][y][break_cnt] + 1
                # 다음이 벽인데 깨고 이동할 수 있는 경우
                elif arr[cx][cy] == 1 and break_cnt == 0:
                    q.append((cx, cy, break_cnt + 1))
                    visited[cx][cy][1] = visited[x][y][0] + 1
    return -1
                
answer = bfs()
print(answer)
