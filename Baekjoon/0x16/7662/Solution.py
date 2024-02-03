from sys import stdin
from heapq import heappop, heappush     # 우선 순위 큐 사용

T = int(input())

for _ in range(T):
    k = int(stdin.readline().rstrip())
    min_heap = []
    max_heap = []
    is_exist = [False] * k  # i번째 삽입된 노드가 존재하는지

    for i in range(k):
        command, num = stdin.readline().split()
        n = int(num)

        if(command == 'I'):
            heappush(min_heap, (n, i))   # 최소 힙 (n, i)
            heappush(max_heap, (-n, i))     # 최대 힙 (-n, i)
            is_exist[i] = True
        elif(n == 1):
            # 이미 삭제된 노드 제거
            while (max_heap and not is_exist[max_heap[0][1]]):
                heappop(max_heap)
            # 최대힙의 첫번째 노드 제거
            if max_heap:
                val, idx = heappop(max_heap)
                is_exist[idx] = False
        else:
            # 이미 삭제된 노드 제거
            while (min_heap and not is_exist[min_heap[0][1]]):
                heappop(min_heap)
            # 최소힙의 첫번째 노드 제거
            if min_heap:
                val, idx = heappop(min_heap)
                is_exist[idx] = False

        # min heap, max heap 동기화
        while (min_heap and not is_exist[min_heap[0][1]]):
            heappop(min_heap)
        while (max_heap and not is_exist[max_heap[0][1]]):
            heappop(max_heap)
        
    if(min_heap and max_heap):
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
