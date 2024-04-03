from sys import stdin
from collections import deque
from heapq import heappop, heappush

INF = int(2e9)
N, M = map(int, input().split())
# 학급 별 능력치 순으로 정렬
students = [deque(sorted(list(map(int, stdin.readline().split())))) for _ in range(N)]
mn = INF
mx = 0
min_heap = []

# 학급 별 능력치가 가장 작은 학생을 뽑는다
# 해당 학생들을 최소힙에 넣는다
for i in range(len(students)):
    v = students[i].popleft()
    mx = max(mx, v)
    mn = min(mn, v)
    heappush(min_heap, [v, i])

result = mx - mn

while min_heap:
    v, pos = heappop(min_heap)
    
    # 하나의 학급에서 더이상 비교할 학생이 없다면 탈출
    if not students[pos]:
        break

    # 최소힙에서 뽑아낸 학생의 학급에서, 해당 학생 다음으로 능력치가 낮은 학생을 뽑는다
    # 해당 학생을 최소힙에 넣는다
    new_v = students[pos].popleft()
    heappush(min_heap, [new_v, pos])
    mx = max(mx, new_v)
    mn = min_heap[0][0]
    result = min(result, mx - mn)

print(result)
