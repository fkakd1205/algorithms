from sys import stdin
from heapq import heappush, heappop

N = int(input())
times = [list(map(int, stdin.readline().split())) for _ in range(N)]
times.sort()    # 시작 시간 순 정렬
min_heap = [(0, 0)]     # 종료 시간 순 min heap

for i in range(N):
    prev = min_heap[0][0]
    # 제일 빨리 종료되는 것보다 늦게 시작한다면
    if times[i][0] >= prev:
        heappop(min_heap)
    heappush(min_heap, (times[i][1], times[i][0]))
        
print(len(min_heap))
