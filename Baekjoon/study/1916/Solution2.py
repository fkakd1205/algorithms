from sys import stdin
from heapq import heappush, heappop

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
min_heap = []
checked = [False] * (N+1)

for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    adj[a].append((c, b))

st, en = map(int, input().split())
checked[st] = True

for cost, next in adj[st]:
    heappush(min_heap, (cost, next))

while min_heap:
    c, n = heappop(min_heap)
    if checked[n]: continue
    if n == en:
        print(c)
        break

    checked[n] = True
    for cost, next in adj[n]:
        if checked[next]: continue
        heappush(min_heap, (cost+c, next))
