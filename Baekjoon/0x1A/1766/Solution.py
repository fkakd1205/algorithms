from sys import stdin
from heapq import heappush, heappop

# 4 2
# 1 4
# 3 2
# ans => 1 3 2 4 (1 4 3 2 아님)
N, M = map(int, input().split())
quest = [i for i in range(1, N+1)]
adj = [[] for _ in range(N+1)]
deg = [0] * (N+1)
min_heap = []   # 3번 조건을 만족하기 위해 

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    adj[a].append(b)
    deg[b] += 1

def bfs():
    while min_heap:
        cur = heappop(min_heap)
        print(cur, end=' ')

        for ad in adj[cur]:
            if deg[ad] == 0: continue
            deg[ad] -= 1
            if deg[ad] == 0:
                heappush(min_heap, ad)

for i in range(N, 0, -1):
    if deg[i] == 0:
        heappush(min_heap, i)

bfs()
