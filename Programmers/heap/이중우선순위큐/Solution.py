from heapq import heappush, heappop

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    deleted = []

    for i in range(len(operations)):
        oper, value = operations[i].strip().split(' ')
        
        if oper == 'I':
            heappush(min_heap, (int(value), i))
            heappush(max_heap, (-int(value), i))
        elif value == '1':
            if max_heap:
                _, idx = heappop(max_heap)
                deleted.append(idx)
        else:
            if min_heap:
                _, idx = heappop(min_heap)
                deleted.append(idx)

        # 동기화
        while(max_heap and max_heap[0][1] in deleted): heappop(max_heap)
        while(min_heap and min_heap[0][1] in deleted): heappop(min_heap)

    if (len(min_heap) + len(max_heap) == 0):
        answer = [0, 0]
    else:
        mx = heappop(max_heap)
        mn = heappop(min_heap)
        answer = [-mx[0], mn[0]]

    return answer

N = int(input())
operations = input().split(',')
print(solution(operations))
