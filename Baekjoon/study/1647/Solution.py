from sys import stdin
from heapq import heappush, heappop

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
min_heap = []
sum = 0
last_cost = 0

for _ in range(M):
    u, v, c = map(int, stdin.readline().split())
    heappush(min_heap, (c, u, v))

def find_p(x):
    x_p = parent[x]

    if x_p != x:
        parent[x] = find_p(x_p)
    
    return parent[x]

def union_p(x, y):
    x_p = find_p(x)
    y_p = find_p(y)

    if x_p < y_p:
        parent[y_p] = x_p
    else:
        parent[x_p] = y_p

# 비용이 작은 경로를 합치다가 마지막 경로만 제거
while min_heap:
    cost, a, b = heappop(min_heap)

    if find_p(a) != find_p(b):
        union_p(a, b)
        sum += cost
        last_cost = cost

print(sum - last_cost)
