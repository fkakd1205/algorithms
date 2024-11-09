from sys import stdin
from heapq import heappush, heappop

T = int(input())

for _ in range(T):
    N, K = map(int, stdin.readline().split())
    costs = [0] + list(map(int, stdin.readline().split()))

    adj = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    min_heap = []

    for _ in range(K):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        indegree[v] += 1
    
    W = int(stdin.readline().rstrip())

    for i in range(1, N+1):
        if indegree[i] == 0:
            heappush(min_heap, (costs[i], i))

    while min_heap:
        delay, cur = heappop(min_heap)

        if cur == W:
            print(delay)
            break

        for ad in adj[cur]:
            indegree[ad] -= 1
            if indegree[ad] == 0:
                heappush(min_heap, (delay + costs[ad], ad))
