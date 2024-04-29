from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
cost = [[INF] * (N+1) for _ in range(N+1)]
min_heap = []
result = 0

for _ in range(M):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((c, v))

def dijkstra(st):
    cost[st][st] = 0
    heappush(min_heap, (cost[st][st], st))

    while min_heap:
        dis, cur = heappop(min_heap)
        if cost[st][cur] < dis: continue

        for d, ad in adj[cur]:
            if cost[st][ad] < dis + d: continue
            cost[st][ad] = dis + d
            heappush(min_heap, (cost[st][ad], ad))

# 최단경로 - 다익스트라 알고리즘
for i in range(1, N+1):
    dijkstra(i)

# i -> X -> i 최단경로의 최대값 구하기
for i in range(1, N+1):
    result = max(result, cost[i][X] + cost[X][i])

print(result)
