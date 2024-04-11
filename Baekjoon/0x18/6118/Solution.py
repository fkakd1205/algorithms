from sys import stdin
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [0] * (N+1)

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    q = deque()
    q.append(1)
    dist[1] = 1

    while q:
        cur = q.popleft()

        for ad in graph[cur]:
            if dist[ad] != 0: continue
            dist[ad] = dist[cur] + 1
            q.append(ad)

bfs()
mx = max(dist)
result = []
cnt = 0
for i in range(1, N+1):
    if mx == dist[i]:
        result.append(i)
        cnt += 1

print(result[0], mx-1, len(result))
    

