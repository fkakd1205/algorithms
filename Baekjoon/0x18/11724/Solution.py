from sys import stdin
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

# 양방향 그래프
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs():
    global count

    for i in range(1, N+1):
        if visited[i]: continue
        count += 1
        q = deque()
        q.append(i)
        visited[i] = True
        
        while(q):
            cur = q.popleft()
            for a in adj[cur]:
                if visited[a]: continue
                q.append(a)
                visited[a] = True

bfs()
print(count)