from sys import stdin
from heapq import heappush, heappop

N = int(input())
min_heap = []
check = [False] * (N+1)
adj = [[] for _ in range(N+1)]
result = 0

# 우물을 파는 것. 목적지 0으로 설정
for i in range(1, N+1):
    cost = int(stdin.readline().rstrip())
    heappush(min_heap, (cost, i))
    adj[0].append((cost, i))
    adj[1].append((cost, 0))

check[0] = True
costs = [list(map(int, stdin.readline().split())) for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if costs[i-1][j-1] == 0: continue
        adj[i].append((costs[i-1][j-1], j))

while (sum(check) <= N and min_heap):
    c, des = heappop(min_heap)
    if check[des] : continue
    result += c
    check[des] = True

    # 물을 대고 난 후 그 주변 논에서 뮬울 끌어오는 비용
    for ad_c, ad_des in adj[des]:
        if check[ad_des]: continue
        heappush(min_heap, (ad_c, ad_des))

print(result)
