from sys import stdin
from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, d = map(int, stdin.readline().split())
    tree[u].append((v, d))
    tree[v].append((u, d))

def bfs(st):
    distance = [0] * (N+1)
    q = deque()
    q.append(st)
    mx = 0

    while q:
        cur = q.popleft()

        for ad, next_d in tree[cur]:
            if ad == st or distance[ad] != 0: continue
            q.append(ad)
            distance[ad] = distance[cur] + next_d
            mx = max(mx, distance[ad])

    return distance.index(mx), mx

# 1. 임의의 점에서 가장 먼 점을 구하고 -> a
# 2. (1)에서 구한 점에서 가장 먼 점을 구하면 -> b
# 3. 이 a, b가 트리에서 가장 먼 두 점이 된다
answer = bfs(bfs(1)[0])[1]
print(answer)
