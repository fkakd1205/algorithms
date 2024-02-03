from sys import stdin
from heapq import heappush, heappop

N, K = map(int, input().split())
max_heap = []

for _ in range(N):
    weight, value = map(int, stdin.readline().split())
    heappush(max_heap, (weight, value))

C = [int(stdin.readline().rstrip()) for _ in range(K)]

# 허용 무게가 작은 가방부터 담아야한다
# 큰 가방을 먼저 채우면 이후에 나오는 보석(무겁고 값 비싼)을 담지 못한다
C.sort()

sum = 0
temp_heap = []
for max_w in C:
    # 가방에 담을 수 있는 보석들의 무게들로 다시 최대힙 생성
    while(max_heap and max_heap[0][0] <= max_w):
        weight = -heappop(max_heap)[1]
        heappush(temp_heap, weight)
    if temp_heap:
        sum -= heappop(temp_heap)

print(sum)
