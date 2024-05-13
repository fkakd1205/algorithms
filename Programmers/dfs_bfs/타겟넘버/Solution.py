from collections import deque

nums = []
t = 0
cnt = 0

def bfs(cur):
    global cnt

    q = deque()
    q.append((nums[cur], cur))
    q.append((-nums[cur], cur))

    while q:
        n, cur = q.popleft()
        
        if cur == len(nums)-1:
            if t == n:
                cnt += 1
            continue

        q.append((n + nums[cur+1], cur + 1))
        q.append((n - nums[cur+1], cur + 1))

def solution(numbers, target):
    global nums, t, cnt
    answer = 0
    nums = numbers
    t = target
    bfs(0)
    answer = cnt
    return answer

numbers = list(map(int, input().split()))
target = int(input())
print(solution(numbers, target))
