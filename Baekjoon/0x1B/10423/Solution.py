from sys import stdin
from heapq import heappush, heappop

N, M, K = map(int, input().split())
plant = list(map(int, stdin.readline().split()))
adj = [[] for _ in range(N+1)]
check = [False] * (N+1)
min_heap = []
result = 0

for _ in range(M):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((c, v))
    adj[v].append((c, u))

# 발전소와 인접한 노드들을 최소힙에 넣는다
for p in plant:
    check[p] = True
    for c, ad in adj[p]:
        heappush(min_heap, (c, ad))

# 최소힙에서 하나씩 꺼내 연결한다
# 꺼낸 노드에서 인접한 노드들을 또 최소힙에 넣는다
while (sum(check) < N and min_heap):
    cost, city = heappop(min_heap)
    if check[city]: continue
    check[city] = True
    result += cost

    for c, ad in adj[city]:
        if check[ad]: continue
        heappush(min_heap, (c, ad))

print(result)
