from sys import stdin
from heapq import heappush, heappop

V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]
result = [-1] * (V+1)
min_heap = []

for _ in range(E):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((c, v))

result[K] = 0
for cost, des in adj[K]:
    heappush(min_heap, (cost, des))

while min_heap:
    c, d = heappop(min_heap)
    if result[d] != -1: continue
    result[d] = c

    for cost, des in adj[d]:
        heappush(min_heap, (c + cost, des))

for i in range(1, V+1):
    if result[i] == -1:
        print("INF")
    else:
        print(result[i])