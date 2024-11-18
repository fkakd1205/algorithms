from sys import stdin
from heapq import heappush, heappop

min_heap = []
max_heap = []

N = int(input())

for _ in range(N):
    value = int(stdin.readline().rstrip())

    if max_heap and value < -max_heap[0]:
        heappush(max_heap, -value)
        if len(min_heap) + 1 < len(max_heap):
            heappush(min_heap, -heappop(max_heap))
    else:
        heappush(min_heap, value)
        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))

    # 중간값은 항상 max_heap에 0번째에 위치하도록
    print(-max_heap[0])
