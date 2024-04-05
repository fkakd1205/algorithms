from sys import stdin
from heapq import heappop, heappush

N, K = map(int, input().split())
min_heap = []

for i in range(N):
    M, V = map(int, stdin.readline().split())
    heappush(min_heap, (M, V))

C = [int(stdin.readline().rstrip()) for _ in range(K)]
C.sort()

cost = 0
max_heap = []
for i in range(K):
    # 현재 가방에 담을 수 있는 보석 중 가치가 높은 보석을 찾는다
    while(min_heap and min_heap[0][0] <= C[i]):
        value = heappop(min_heap)[1]
        heappush(max_heap, -value)
    if max_heap:
        cost -= heappop(max_heap)

print(cost)
