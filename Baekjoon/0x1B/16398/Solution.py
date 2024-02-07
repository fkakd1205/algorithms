from sys import stdin
from heapq import heappush, heappop

N = int(input())
cost = [list(map(int, stdin.readline().split())) for _ in range(N)]
adj = [[] for _ in range(N+1)]
check = [False] * (N+1)
count = 0
min_heap = []
total_cost = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        adj[i].append([cost[i-1][j-1], j])

# 임의의 점 선택
check[1] = True
for ad in adj[1]:
    heappush(min_heap, [ad[0], ad[1]])

# 프림 알고리즘
# 현재 노드에서 연결된 노드의 [가중치, 번호]를 최소힙에 넣어 최소 가중치합을 구한다
while(count < N-1):
    c, des = heappop(min_heap)
    if(check[des]): continue
    count += 1
    total_cost += c
    check[des] = True

    for ad in adj[des]:
        if(check[ad[1]]): continue
        heappush(min_heap, [ad[0], ad[1]]) 

print(total_cost)
