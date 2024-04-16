from sys import stdin
from collections import deque

N = int(input())
names = list(map(str, stdin.readline().split()))

M = int(input())
adj = dict()
deg = dict()
result = dict()
q = deque()

for n in names:
    adj[n] = []
    deg[n] = 0
    result[n] = []

for _ in range(M):
    child, parent = map(str, stdin.readline().split())

    adj[parent].append(child)
    deg[child] += 1

def bfs():
    while q:
        cur = q.popleft()

        for ad in adj[cur]:
            if deg[ad] == 0: continue
            deg[ad] -= 1
            if deg[ad] == 0:
                q.append(ad)
                result[cur].append(ad)

for name in deg:
    if (deg[name] == 0):
        q.append(name)

print(len(q))
print(*sorted(list(q)))
bfs()

sorted_result = sorted(result.items(), key=lambda x: x[0])

for key, value in sorted_result:
    value.sort()
    print(key, len(value), *value)
