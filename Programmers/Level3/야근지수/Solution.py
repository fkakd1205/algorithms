from heapq import heappop, heappush

def solution(n, works):
    answer = 0
    max_heap = []
    for work in works:
        heappush(max_heap, -work)
    
    while n > 0:
        work = -heappop(max_heap)

        if work == 0: break
        work -= 1
        heappush(max_heap, -work)        
        n -= 1

    if max_heap:
        answer = sum([(work ** 2) for work in max_heap])
    return answer

n = int(input())
works = list(map(int, input().split()))
print(solution(n, works))
