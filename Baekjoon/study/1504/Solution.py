from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, stdin.readline().split())

def dijkstra(st):
    min_heap = []
    dist = [INF] * (N+1)
    dist[st] = 0
    heappush(min_heap, (0, st))

    while min_heap:
        cost, cur = heappop(min_heap)
        
        if dist[cur] != cost: continue
        
        for ad, c in adj[cur]:
            if cost + c < dist[ad]:
                dist[ad] = cost+c
                heappush(min_heap, (cost+c, ad))
    return dist

dijk_start = dijkstra(1)
dijk_v1 = dijkstra(v1)
dijk_v2 = dijkstra(v2)

# [1 -> v1 -> v2 -> N] or [1 -> v2 -> v1 -> N]
mn = min(dijk_start[v1] + dijk_v1[v2] + dijk_v2[N], dijk_start[v2] + dijk_v2[v1] + dijk_v1[N])

if mn >= INF:
    print(-1)
else:
    print(mn)
