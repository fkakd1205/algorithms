from sys import stdin
from heapq import heappush, heappop

N = int(input())
heap = []

# 메모리 초과
# for _ in range(N):
#     nums = map(int, stdin.readline().split())

#     for n in nums:
#         heappush(heap, -n)

# for _ in range(N-1):
#     heappop(heap)

# print(-heap[0])

# 최대값 N개 까지만 heap에 담는다
for _ in range(N):
    nums = map(int, stdin.readline().split())

    for n in nums:
        if(len(heap) < N):
            heappush(heap, n)
        else:
            # heap에 있는 최솟값보다 n이 더 큰 경우, heap의 최솟값을 제거하고 n을 넣는다
            if(n > heap[0]):
                heappop(heap)
                heappush(heap, n)

print(heap[0])
