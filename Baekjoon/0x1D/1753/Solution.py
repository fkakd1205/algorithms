from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)

V, E = map(int, input().split())
st = int(input())

adj = [[] for _ in range(V+1)]
d = [INF] * (V+1)
min_heap = []

for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    adj[u].append([w, v])

# 다익스트라 알고리즘
d[st] = 0
heappush(min_heap, [d[st], st])
while(min_heap):
    cur = heappop(min_heap)
    if cur[0] != d[cur[1]]: continue    # 이미 최단경로가 결정되었다면 
    for ad in adj[cur[1]]:
        if d[ad[1]] <= cur[0] + ad[0]: continue
        # 경유해서 이동하는 경로가 더 짧다면, d 갱신
        d[ad[1]] = cur[0] + ad[0]
        heappush(min_heap, [d[ad[1]], ad[1]])

for i in range(1, V+1):
    if d[i] == INF: print("INF")
    else: print(d[i])
