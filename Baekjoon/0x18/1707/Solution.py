from sys import stdin
from collections import deque

T = int(input())
q = deque()

def bfs(start, group):
    q.append((start, group))
    check[start] = group
    is_bipartitie = True

    while q:
        x, g = q.popleft()

        for ad in adj[x]:
            # 인접한 노드가 같은 그룹에 속하는 경우
            if check[ad] == g:
                is_bipartitie = False
                break
            # 인접한 노드가 같은 그룹에 속하지 않는 경우
            if check[ad] == -g: continue
            check[ad] = -g
            q.append((ad, -g))
            
    return is_bipartitie

for _ in range(T):
    V, E = map(int, stdin.readline().split())
    adj = [[] for _ in range(V+1)]
    check = [0] * (V+1)
    is_bipartitie_graph = True

    for _ in range(E):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    
    for i in range(1, V+1):
        if check[i]: continue
        if(not bfs(i, 1)):
            is_bipartitie_graph = False
            break
    
    if is_bipartitie_graph:
        print("YES")
    else:
        print("NO")
