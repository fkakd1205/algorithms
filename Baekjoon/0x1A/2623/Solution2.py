from sys import stdin
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
deg = [0] * (N+1)
q = deque()
result = []

for _ in range(M):
    nums = list(map(int, stdin.readline().split()))
    
    for i in range(1, nums[0]):
        adj[nums[i]].append(nums[i+1])
        deg[nums[i+1]] += 1

def bfs():
    while q:
        cur = q.popleft()
        result.append(cur)

        for ad in adj[cur]:
            if deg[ad] == 0: continue
            deg[ad] -= 1
            if deg[ad] == 0:
                q.append(ad)

for i in range(1, N+1):
    if deg[i] == 0:
        q.append(i)

bfs()

if sum(deg) == 0:
    print(*result, sep='\n')
else:
    print(0)
