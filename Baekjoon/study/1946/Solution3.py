from sys import stdin
from heapq import heappush

T = int(input())


for _ in range(T):
    N = int(input())
    score = [list(map(int, stdin.readline().split())) for _ in range(N)]
    score.sort(key= lambda x: x[0])
    mn_heap = []
    pass_cnt = 0

    # 이미 정렬된 상태에서, score2에 대해서 자신이 더 높은 순위라면 합격
    for _, s2 in score:
        heappush(mn_heap, s2)
        if s2 == mn_heap[0]:
            pass_cnt += 1

    print(pass_cnt)
