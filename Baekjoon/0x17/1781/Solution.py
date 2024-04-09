from sys import stdin
from heapq import heappush, heappop

N = int(input())
quest = [list(map(int, stdin.readline().split())) for _ in range(N)]
min_heap = []

# 데드라인이 빠른 순으로 정렬
quest.sort()

for d, c in quest:
    heappush(min_heap, c)
    
    # min_heap의 사이즈를 데드라인으로 생각
    # 문제 데드라인이 빠른 순으로 컵라면을 많이 가져갈 수 있는 것을 선택한다
    if d < len(min_heap):
        heappop(min_heap)

print(sum(min_heap))
