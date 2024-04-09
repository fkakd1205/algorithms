from sys import stdin
from collections import deque

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs():
    visited = [False] * (N+1)

    stack = [V]

    while stack:
        k = stack.pop()

        if visited[k]: continue
        visited[k] = True
        print(k, end=' ')

        for ad in adj[k]:
            if visited[ad]: continue
            stack.append(ad)

def bfs():
    visited = [False] * (N+1)
    q = deque()
    
    q.append(V)
    visited[V] = True
    print(V, end=' ')

    while q:
        k = q.popleft()

        for ad in adj[k]:
            if visited[ad]: continue
            visited[ad] = True
            q.append(ad)
            print(ad, end=' ')

for i in range(1, N+1):
    adj[i].sort(reverse=True)

dfs()
print()

for i in range(1, N+1):
    adj[i].sort()

bfs()
