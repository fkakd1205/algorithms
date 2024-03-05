from sys import stdin
from collections import deque
from copy import deepcopy

INF = int(1e9)
N = int(input())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs_for_numbering(x, y, n):
    global graph

    q = deque()
    q.append((x, y))
    graph[x][y] = n
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if(0 <= cx < N and 0 <= cy < N and not visited[cx][cy] and graph[cx][cy] != 0):
                q.append((cx, cy))
                graph[cx][cy] = n
                visited[cx][cy] = True

def bfs_for_bridge(n):
    q2 = deque()
    dist = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == n:
                visited[i][j] = True
                q2.append((i, j))
    
    while q2:
        x, y = q2.popleft()

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if (0 <= cx < N and 0 <= cy < N):
                # 다른 섬과 만났다면
                if (graph[cx][cy] != 0 and graph[cx][cy] != n):
                    return dist[x][y]
                # 물이면서 아직 다리가 없는 곳
                elif (graph[cx][cy] == 0 and dist[cx][cy] == 0):
                    dist[cx][cy] = dist[x][y] + 1
                    q2.append((cx, cy))
                    
    return INF

# 섬 번호 설정
number = 1
for i in range(N):
    for j in range(N):
        if (visited[i][j] or graph[i][j] == 0): continue
        bfs_for_numbering(i, j, number)
        number += 1

# 섬 마다 다른 섬으로 가는 다리의 최소 길이 구하기
min_bridge_len = INF
for n in range(1, number):
    min_bridge_len = min(min_bridge_len, bfs_for_bridge(n))

print(min_bridge_len)
