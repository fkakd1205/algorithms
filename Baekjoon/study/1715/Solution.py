from sys import stdin
from heapq import heappush, heappop

N = int(input())
cards = [int(stdin.readline().rstrip()) for _ in range(N)]
min_heap = []
answer = 0

for card in cards:
    heappush(min_heap, card)

while len(min_heap) >= 2:
    a = heappop(min_heap)
    b = heappop(min_heap)
    sum = a + b
    answer += sum
    heappush(min_heap, sum)

print(answer)
