from bisect import bisect_left

def solution(citations):
    answer = 0
    citations.sort()

    for i in range(1, citations[-1]):
        idx = bisect_left(citations, i)
        if (idx > len(citations) // 2):
            break
        if (idx <= len(citations) - i):
            answer = i

    return answer

citations = list(map(int, input().split()))
print(solution(citations))
