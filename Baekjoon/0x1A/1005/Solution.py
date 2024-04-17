from sys import stdin
from collections import deque

T = int(input())

def bfs():
    while q:
        num, t = q.popleft()

        if num == W:
            return t

        for ad in adj[num]:
            if deg[ad] == 0: continue
            deg[ad] -= 1
            memo[ad].append(t)
            if deg[ad] == 0:
                q.append((ad, max(memo[ad]) + time[ad]))

for _ in range(T):
    N, K = map(int, stdin.readline().split())
    time = [0] + list(map(int, stdin.readline().split()))
    adj = [[] for _ in range(N+1)]
    deg = [0] * (N+1)
    memo = [[] for _ in range(N+1)]
    q = deque()

    for i in range(K):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        deg[v] += 1
    
    W = int(input())

    for i in range(1, N+1):
        if deg[i] == 0:
            q.append((i, time[i]))

    print(bfs())
