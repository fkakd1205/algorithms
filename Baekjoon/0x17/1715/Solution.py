from sys import stdin
from heapq import heappush, heappop

N = int(input())
min_heap = []
count = 0

for _ in range(N):
    heappush(min_heap, int(stdin.readline()))
    
# 가장 작은 개수의 두 카드 묶음을 선택해서 더해야 비교 횟수가 작아진다.
while(len(min_heap) > 1):
    a = heappop(min_heap)
    b = heappop(min_heap)
    sum = a + b
    # 두 카드 묶음을 합쳐서 하나로 만든 후 다시 넣는다
    heappush(min_heap, sum)
    count += sum

print(count)
