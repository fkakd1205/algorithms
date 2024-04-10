from sys import stdin
from collections import deque

INF = int(1e9)
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
q = deque()

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    check = [0] * (N+1)
    for ad in adj[start]:
        q.append(ad)
        check[ad] = 1
    
    check[start] = -1
    while q:
        cur = q.popleft()

        for ad in adj[cur]:
            if check[ad] != 0: continue
            check[ad] = check[cur] + 1
            q.append(ad)

    return sum(check)

mn = INF
mn_idx = -1
for i in range(1, N+1):
    result = bfs(i)
    if result < mn:
        mn = result
        mn_idx = i

print(mn_idx)
