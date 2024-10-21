from sys import stdin
from collections import deque

T = int(input())

def bfs(cur):
    q = deque()
    q.append((cur, 1))
    check[cur] = 1
    
    while q:
        cur, group = q.popleft()
        
        for ad in adj[cur]:
            # 이미 방문했으며, 인접하지 않은 정점이라면
            if check[ad] == -group:
                continue
            # 이미 방문했으며, 자신과 인접한 정점이라면
            if check[ad] == group:
                return True
            check[ad] = -group
            q.append((ad, -group))

    return False

for _ in range(T):
    V, E = map(int, stdin.readline().split())
    adj = [[] for _ in range(V+1)]
    check = [False] * (V+1)
    is_cycle = False

    for _ in range(E):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, V+1):
        if is_cycle: break
        if check[i]: continue
        is_cycle = bfs(i)

    if is_cycle:
        print("NO")
    else:
        print("YES")

    