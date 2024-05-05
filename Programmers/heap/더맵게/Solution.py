from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    min_heap = []

    for score in scoville:
        heappush(min_heap, score)

    while True:
        a = heappop(min_heap)
        if a >= K: break
        if not min_heap:
            answer = -1
            break

        b = heappop(min_heap)
        new_score = a + (b * 2)
        heappush(min_heap, new_score)
        answer += 1

    return answer

scoville = list(map(int, input().split()))
K = int(input())
print(solution(scoville, K))
