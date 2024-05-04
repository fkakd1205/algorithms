from collections import deque

def solution(progresses, speeds):
    answer = []
    arr = deque()

    for progress, speed in zip(progresses, speeds):
        rest = 100 - progress
        # 소요기간 구하기
        if(rest % speed == 0):
            arr.append(rest // speed)
        else:
            arr.append((rest // speed) + 1)
    
    prev = arr.popleft()
    cnt = 1
    while arr:
        cur = arr.popleft()
        if cur <= prev:
            cnt += 1
        else:
            answer.append(cnt)
            prev = cur
            cnt = 1

    answer.append(cnt)
    return answer

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
print(solution(progresses, speeds))
