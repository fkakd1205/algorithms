from sys import stdin
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

q = deque()

for i in range(1, N+1):
    if visited[i]: continue

    visited[i] = True
    q.append(i)
    cnt += 1

    while q:
        k = q.popleft()
        for ad in adj[k]:
            if visited[ad]: continue
            visited[ad] = True
            q.append(ad)

print(cnt)
