from sys import stdin
from collections import deque

def bfs():
    parent = -1

    while q:
        cur = q.popleft()
        
        for ad in tree[cur]:
            if visited[ad] : 
                parent = ad
                continue
            visited[ad] = True
            q.append(ad)
        
        if parent != -1: break

    return parent

T = int(input())
for _ in range(T):
    N = int(stdin.readline().rstrip())
    tree = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    q = deque()

    for _ in range(N-1):
        u, v = map(int, stdin.readline().split())
        tree[v].append(u)
    
    a, b = map(int, stdin.readline().split())
    q.append(a)
    visited[a] = True
    q.append(b)
    visited[b] = True

    print(bfs())
