from sys import stdin
from heapq import heappush, heappop

N = int(input())
min_heap = []
fin_time = 0
answer = 0

for _ in range(N):
    st, en = map(int, stdin.readline().split())
    heappush(min_heap, (en, st))

while min_heap:
    en, st = heappop(min_heap)
    if st >= fin_time:
        fin_time = en
        answer += 1

print(answer)
