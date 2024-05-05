from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque()
    mx = max(priorities)

    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    while q:
        idx, prior = q.popleft()

        if prior == mx:
            if idx == location: break
            priorities[idx] = 0
            answer += 1
            mx = max(priorities)
        else:
            q.append((idx, prior))

    return answer

prior = list(map(int, input().split()))
loc = int(input())
print(solution(prior, loc))
