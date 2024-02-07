from sys import stdin
from heapq import heappush, heappop

N = int(input())
adj = [[] for _ in range(N+1)]
check = [False] * (N+1) # 신장 트리에 속했는지 여부
total_w = 0
min_heap = []
cnt = 0

# 물을 파는 것 = 목적지 0을 임의로 만들어 가중치 설정
for i in range(1, N+1):
    w = int(stdin.readline().rstrip())
    adj[0].append([w, i])
    adj[i].append([w, 0])

cost = [list(map(int, stdin.readline().split())) for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if cost[i-1][j-1] == 0: continue
        adj[i].append([cost[i-1][j-1], j])

check[0] = True
for w, i in adj[0]:
    heappush(min_heap, [w, i])

# 최종 선택된 노드는 N개 (임의의 노드 0을 추가했으므로)
while(cnt < N):
    weight, des = heappop(min_heap)
    if(check[des]): continue
    check[des] = True
    cnt += 1
    total_w += weight

    for w, d in adj[des]:
        if(check[d]): continue
        heappush(min_heap, [w, d])

print(total_w)
