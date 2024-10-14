from sys import stdin
from collections import deque

N = int(input())
M = int(input())
prod_unit = [[] for _ in range(N+1)]
indegree = [0] * (N+1)      # 자신을 부품으로 사용하는 정도
is_base = [True] * (N+1)
count = [0] * (N+1)
q = deque()

for _ in range(M):
    x, y, k = map(int, stdin.readline().split())
    prod_unit[x].append((y, k))
    indegree[y] += 1
    is_base[x] = False

q.append(N)
count[N] = 1

while q:
    cur = q.popleft()

    for unit, k in prod_unit[cur]:
        count[unit] += (count[cur] * k)
        indegree[unit] -= 1
        if indegree[unit] == 0:
            q.append(unit)

for i in range(1, N+1):
    if not is_base[i]: continue
    print(i, count[i])
