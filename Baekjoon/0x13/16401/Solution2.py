from sys import stdin

M, N = map(int, input().split())
nums = list(map(int, stdin.readline().split()))

left = 0
right = max(nums)
answer = 0

def is_divided(target):
    cnt = 0

    for i in range(N):
        if cnt >= M: break
        cnt += nums[i] // target
    
    return cnt >= M

while(left <= right):
    mid = (left + right + 1) // 2   # left = 0, right = 1, mid = 0 인 상황을 배제하기 위해 +1

    if mid == 0: break

    # 나누어 줄 수 있는 경우
    if(is_divided(mid)):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)
