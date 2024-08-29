from sys import stdin
from collections import deque

N, R = map(int, input().split())
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    a, b, d = map(int, stdin.readline().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

q = deque()
q.append((R, 0))
visited[R] = True
is_find = False
total_dis = 0
pole_dis = 0

while q:
    root, d = q.popleft()
    total_dis = max(total_dis, d)
    cnt = 0

    for child, dis in tree[root]:
        if visited[child]: continue
        visited[child] = True
        q.append((child, d + dis))
        cnt += 1

    if cnt >= 2 and not is_find:
        pole_dis = d
        is_find = True

# 가지가 존재하지 않으면 기둥길이가 total_dis
if not is_find:
    print(total_dis, 0)
else:
    print(pole_dis, total_dis - pole_dis)
