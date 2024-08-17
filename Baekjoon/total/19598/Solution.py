from sys import stdin
from heapq import heappush, heappop

# V1. 시간초과
# N = int(input())
# times = [list(map(int, stdin.readline().split())) for _ in range(N)]
# fins = [-1] * N
# answer = 0
# times.sort()

# for st, en in times:
#     for i in range(len(fins)):
#         if fins[i] <= st:
#             fins[i] = en
#             break

# for i in range(N):
#     if fins[i] > 0:
#         answer += 1

# print(answer)

N = int(input())
times = [list(map(int, stdin.readline().split())) for _ in range(N)]
answer = 0
times.sort()
min_heap = []

for st, en in times:
    if min_heap and min_heap[0] <= st:
        heappop(min_heap)
    heappush(min_heap, en)

print(len(min_heap))
