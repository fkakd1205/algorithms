from sys import stdin
from collections import deque

N = int(input())
name = list(stdin.readline().split())
name.sort()

M = int(input())
adj = {n:[] for n in name}
deg = {n: 0 for n in name}
result = {n: [] for n in name}
anc = []

# 조상부터 큐에 넣어확인해야 하므로, adj는 조상을 기준으로 설정
for _ in range(M):
    u, v = stdin.readline().split()
    deg[u] += 1
    adj[v].append(u)

q = deque()
for i in name:
    if(deg[i] == 0):
        q.append(i)
        anc.append(i)

while(q):
    cur = q.popleft()
    for child in adj[cur]:
        deg[child] -= 1
        if(deg[child] == 0):
            q.append(child)
            result[cur].append(child)   # deg[child]가 0이 되었다는건 현재 child가 직전의 부모(cur)의 연결된 자식이라는 것

print(len(anc))
print(*anc)
for name, child in result.items():
    child.sort()
    print(f'{name} {len(child)} ', end='')
    if(len(child) > 0):
        print(' '.join(child))
    else:
        print()
