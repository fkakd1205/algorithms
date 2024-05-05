from heapq import heapify, heappush, heappop

def solution(jobs):
    answer = 0
    jobs_size = len(jobs)
    heapify(jobs)
    ready_jobs = []
    cur_time = 0

    while True:
        while(jobs and jobs[0][0] <= cur_time):
            start_t, burst_t = heappop(jobs)
            heappush(ready_jobs, (burst_t, start_t))

        if ready_jobs:
            burst_t, start_t = heappop(ready_jobs)
            burst_t = cur_time - burst_t
            cur_time += burst_t
            answer += burst_t + burst_t
        elif jobs:
            cur_time = jobs[0][0]
        else:
            break
    
    answer //= jobs_size
    return answer

N = int(input())
jobs = [list(map(int, input().split())) for _ in range(N)]
print(solution(jobs))