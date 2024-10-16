from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]
costs = [INF] * (V+1)
min_heap = []
cnt = 0

for _ in range(E):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((v, c))

heappush(min_heap, (0, K))

while cnt != V and min_heap:
    w, v = heappop(min_heap)
    if costs[v] != INF:
        continue
    
    costs[v] = w
    cnt += 1

    for en, cost in adj[v]:
        heappush(min_heap, (cost+w, en))

for i in range(1, V+1):
    if costs[i] == INF:
        print("INF")
    else:
        print(costs[i])