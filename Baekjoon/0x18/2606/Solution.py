from sys import stdin
from collections import deque

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
virus = [0] * (N+1)

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs():
    q = deque()
    q.append(1)
    virus[1] = 1

    while(q):
        c = q.popleft()

        for ad in adj[c]:
            if(virus[ad]): continue
            q.append(ad)
            virus[ad] = 1

bfs()
print(sum(virus)-1)
