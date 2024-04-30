from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]
d = [[INF] * (N+1) for _ in range(N+1)]
min_heap = []

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

v1, v2 = map(int, input().split())

def dijstra(st):
    d[st][st] = 0
    heappush(min_heap, (d[st][st], st))

    while min_heap:
        c, cur = heappop(min_heap)
        if d[st][cur] < c: continue

        for cost, ad in adj[cur]:
            if cost + c > d[st][ad]: continue
            d[st][ad] = cost + c
            heappush(min_heap, (d[st][ad], ad))

for i in (1, v1, v2):
    dijstra(i)

result = min(d[1][v1] + d[v1][v2] + d[v2][N], d[1][v2] + d[v2][v1] + d[v1][N])
if result >= INF:
    print(-1)
else:
    print(result)
