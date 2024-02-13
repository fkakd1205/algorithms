from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, stdin.readline().split())
    adj[u].append([w, v])

def func(st, en):
    d = [INF] * (N+1)
    min_heap = []

    d[st] = 0
    heappush(min_heap, [d[st], st])
    while(min_heap):
        cur = heappop(min_heap)
        if cur[0] != d[cur[1]]: continue
        for ad in adj[cur[1]]:
            if(d[ad[1]] <= cur[0] + ad[0]): continue
            d[ad[1]] = cur[0] + ad[0]
            heappush(min_heap, [d[ad[1]], ad[1]])
    
    return d[en]

result = 0
for st in range(1, N+1):
    if(st == X): continue
    result = max(result, func(st, X) + func(X, st))     # 출발지 -> X -> 츨빌지 로 왕복 최소 시간을 구한다

print(result)
