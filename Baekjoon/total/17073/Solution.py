from sys import stdin
from collections import deque

N, W = map(int, input().split())
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)
leaf_cnt = 0

for _ in range(N-1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

q = deque()
q.append(1)
visited[1] = True

while q:
    root = q.popleft()
    is_leaf = True

    for child in tree[root]:
        if visited[child]: continue
        q.append(child)
        visited[child] = True
        is_leaf = False
    
    if is_leaf:
        leaf_cnt += 1

print(round(W / leaf_cnt, 6))
