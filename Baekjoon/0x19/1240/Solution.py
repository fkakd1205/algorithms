from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

N, M = map(int, stdin.readline().split())
tree = [[] for _ in range(N+1)]
ds = [0 for _ in range(N+1)]

for _ in range(N-1):
    x, y, z = map(int, stdin.readline().split())
    tree[x].append((y, z))
    tree[y].append((x, z))

def search_dis(start, finish):
    queue = deque()
    queue.append((start, 0))

    visited = [False for _ in range(N+1)]
    visited[start] = True

    while queue:
        node, dis = queue.popleft()
        
        if (node == finish):
            return dis
        
        for i, d in tree[node]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, dis + d))

for _ in range(M):
    x, y = map(int, stdin.readline().split())
    print(search_dis(x, y))
