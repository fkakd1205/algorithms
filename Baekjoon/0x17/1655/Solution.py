from sys import stdin
from heapq import heappop, heappush

N = int(input())
l_heap = []
r_heap = []

for _ in range(N):
    num = int(stdin.readline().rstrip())

    # 처음 입력된 숫자를 left_heap에 넣는다
    if not l_heap:
        heappush(l_heap, -num)
        print(num)
        continue
    
    # left_heap[0]보다 큰 값이 입력되면 right_heap에 넣는다
    if (-l_heap[0] < num):
        heappush(r_heap, num)
    else:
        heappush(l_heap, -num)
    
    # left_heap과 right_heap의 사이즈를 비교해 균형을 맞춘다
    if (len(l_heap) < len(r_heap)):
        x = heappop(r_heap)
        heappush(l_heap, -x)
    elif (len(l_heap) > len(r_heap) + 1):
        x = -heappop(l_heap)
        heappush(r_heap, x)
    
    print(-l_heap[0])
