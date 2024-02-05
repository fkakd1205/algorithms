from sys import stdin
from collections import deque

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):
    adj[i].sort()

# 비재귀 DFS
def dfs1(st):
    s = []
    s.append(st)

    # append 후 visited 여부를 변경하지 않고, 꺼낸 후 visited 여부를 변경
    # 스택에 중복 node가 들어갈 수 있지만 관념적인 DFS 순서를 따를 수 있다.
    while(s):
        cur = s.pop()
        if(visited[cur]): continue
        visited[cur] = True 
        print(cur, end=' ')

        # stack이니 작은수를 마지막에 넣어야 함
        for i in range(len(adj[cur])):
            a = adj[cur][len(adj[cur])-1-i]
            if(visited[a]): continue
            s.append(a)
    

# 재귀 DFS
def dfs2(st):
    visited[st] = True
    print(st, end=' ')
    
    for a in adj[st]:
        if(visited[a]): continue
        dfs2(a)

def bfs():
    q = deque()
    q.append(V)
    visited[V] = True

    while(q):
        cur = q.popleft()
        print(cur, end=' ')

        for a in adj[cur]:
            if visited[a]: continue
            q.append(a)
            visited[a] = True

# dfs2(V)
dfs1(V)
print()
visited = [False] * (N+1)
bfs()