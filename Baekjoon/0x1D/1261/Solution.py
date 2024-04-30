from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
N, M = map(int, input().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(M)]
dist = [[INF] * N for _ in range(M)]
min_heap = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dist[0][0] = 0
heappush(min_heap, (dist[0][0], 0, 0))

def dijkstra():
    while min_heap:
        d, x, y = heappop(min_heap)
        if dist[x][y] < d: continue

        if x == M-1 and y == N-1: break     # arr[M][N]에 도달하면 종료

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if (0 <= cx < M and 0 <= cy < N):
                if (dist[cx][cy] <= d + arr[cx][cy]): continue
                dist[cx][cy] = d + arr[cx][cy]
                heappush(min_heap, (dist[cx][cy], cx, cy))      # 0을 우선으로 경로를 선택하도록 함

dijkstra()
print(dist[M-1][N-1])
