from sys import stdin
from heapq import heappush, heappop

INF = int(1e9)
n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
d = [INF] * (n+1)
pre = [0] * (n+1)
min_heap = []
path = []

for _ in range(m):
    u, v, c = map(int, stdin.readline().split())
    adj[u].append((c, v))

st, en = map(int, input().split())

d[st] = 0
heappush(min_heap, (d[st], st))

while min_heap:
    cost, cur = heappop(min_heap)
    if d[cur] < cost: continue  # 이미 설정된 최소비용보다 크다면 pass

    for c, ad in adj[cur]:
        if (d[ad] <= c + cost): continue
        d[ad] = cost + c
        pre[ad] = cur
        heappush(min_heap, (d[ad], ad))

cur = en
path.append(cur)
while(cur != st):
    path.append(pre[cur])
    cur = pre[cur]
path.reverse()

print(d[en])
print(len(path))
print(*path)
