from sys import stdin
from heapq import heappush, heappop

N = int(input())
quest = [list(map(int, stdin.readline().split())) for _ in range(N)]
min_heap = []

quest.sort()

for day, cnt in quest:
    heappush(min_heap, cnt)

    # 현재 작업의 데드라인이 4일이라면 힙에 최대 4개의 작업만 포함시켜야 한다
    if day < len(min_heap):
        heappop(min_heap)

print(sum(min_heap))
