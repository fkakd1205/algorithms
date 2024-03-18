from sys import stdin
from heapq import heappush, heappop

N = int(input())
time = [list(map(int, stdin.readline().split())) for _ in range(N)]
time.sort()
heap = []

heappush(heap, time[0][1])  # 끝나는 시간이 빠른 순
cnt = 1

for i in range(1, N):
    # 시작시간이 끝나는 시간보다 크거나 같은 경우 (강의실 공유)
    if heap[0] <= time[i][0]:
        heappop(heap)
        heappush(heap, time[i][1])
    else:
        heappush(heap, time[i][1])
        cnt += 1
    
print(cnt)
