from sys import stdin
from collections import deque

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        k = q.popleft()
        for ad in adj[k]:
            if visited[ad]: continue
            visited[ad] = 1
            q.append(ad)

bfs()
result = sum(visited)
if result == 1:
    print(0)
else:
    print(result - 1)
