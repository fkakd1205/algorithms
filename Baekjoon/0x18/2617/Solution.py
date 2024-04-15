from sys import stdin
from collections import deque

N, M = map(int, input().split())
graph1 = [[] for _ in range(N+1)]   # 자신보다 무거운 노드 추가
graph2 = [[] for _ in range(N+1)]   # 자신보다 가벼운 노드 추가
check = [False] * (N+1)
mid = (N+1) // 2
cnt = 0

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph1[b].append(a)
    graph2[a].append(b)

def bfs(graph, cur):
    check = [False] * (N+1)
    q = deque()
    q.append(cur)
    check[cur] = True
    cnt = 0

    while q:
        x = q.popleft()
        for ad in graph[x]:
            if check[ad]: continue
            q.append(ad)
            check[ad] = True
            cnt += 1

    return cnt

for i in range(1, N+1):
    cnt1 = bfs(graph1, i)
    cnt2 = bfs(graph2, i)

    # 자신보다 무거운 노드가 mid개 이상이거나, 가벼운 노드가 mid개 이상이면
    # 해당 노드는 중간값이 될 수 없다.
    if (cnt1 >= mid or cnt2 >= mid):
        cnt += 1

print(cnt)