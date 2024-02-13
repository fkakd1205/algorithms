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

for i in range(m):
    u, v, w = map(int, stdin.readline().split())
    adj[u].append([w, v])

st, en = map(int, input().split())

# 다익스트라 알고리즘
d[st] = 0
heappush(min_heap, [d[st], st])
while(min_heap):
    cur = heappop(min_heap)
    if cur[0] != d[cur[1]]: continue
    for ad in adj[cur[1]]:
        if (d[ad[1]] <= cur[0] + ad[0]): continue
        d[ad[1]] = cur[0] + ad[0]
        pre[ad[1]] = cur[1]    # 경유지 설정
        heappush(min_heap, [d[ad[1]], ad[1]])

# 도착지를 기준으로 경유지를 찾는다
cur = en
path.append(cur)
while(cur != st):
    path.append(pre[cur])
    cur = pre[cur]
path.reverse()

print(d[en])
print(len(path))
print(*path)
