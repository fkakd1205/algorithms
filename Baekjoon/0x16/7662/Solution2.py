from sys import stdin
from heapq import heappop, heappush
from copy import deepcopy

T = int(input())
deleted_value = []

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    check = [False] * k

    for i in range(k):
        command, n = stdin.readline().split()
        num = int(n)

        if command == 'I':
            heappush(min_heap, (num, i))
            heappush(max_heap, (-num, i))
            check[i] = True
        else:
            if len(min_heap) == 0: continue
            
            if num == 1:
                _, pos = heappop(max_heap)
                check[pos] = False
            else:
                _, pos = heappop(min_heap)
                check[pos] = False

            # 동기화
            while(min_heap and not check[min_heap[0][1]]):
                heappop(min_heap)
            while(max_heap and not check[max_heap[0][1]]):
                heappop(max_heap)

    
    if len(min_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
