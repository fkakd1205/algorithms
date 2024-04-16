from sys import stdin
from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N+1)
tree = [[] for _ in range(N+1)]
q = deque()

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    indegree[v] += 1
    tree[u].append(v)

def bfs():
    while q:
        cur = q.popleft()

        for next in tree[cur]:
            if indegree[next] == 0: continue
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
                print(next, end=' ')

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        print(i, end=' ')

bfs()