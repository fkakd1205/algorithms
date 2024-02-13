from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)

N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    adj[a].append([c, b])
    adj[b].append([c, a])

v1,v2 = map(int, input().split())

def dijkstra(st):
    d = [INF] * (N+1)
    min_heap = []

    d[st] = 0
    heappush(min_heap, [d[st], st])
    while(min_heap):
        cur = heappop(min_heap)
        if d[cur[1]] != cur[0]: continue
        for ad in adj[cur[1]]:
            if (d[ad[1]] <= cur[0] + ad[0]): continue
            d[ad[1]] = cur[0] + ad[0]
            heappush(min_heap, [d[ad[1]], ad[1]])

    return d

# 1, v1, v2이 출발점일 때 최단 거리
dis1 = dijkstra(1)
dis2 = dijkstra(v1)
dis3 = dijkstra(v2)

route1 = dis1[v1] + dis2[v2] + dis3[N]  # 1 -> v1 -> v2 -> N
route2 = dis1[v2] + dis3[v1] + dis2[N]  # 1 -> v2 -> v1 -> N

result = min(route1, route2)

# result가 INF보다 큰 경우 갈 수 있는 경로가 없다
if(result >= INF):
    print(-1)
else:
    print(result)
