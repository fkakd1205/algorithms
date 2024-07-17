from sys import stdin

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
result = [0] * M
is_used = [False] * N

nums.sort()

# V1. 틀림
# 4 3
# 1 3 9 9
# 출력에서 3 1 9 이 아닌 3 9 1이 바로 출력
# 이전에 출력된 result와 현재 세팅하는 reuslt도 비교하므로 result[cur] == nums[i] 잘못된 코드
# def recur(cur):
#     if cur == M:
#         print(*result)
#         return
    
#     for i in range(N):
#         if is_used[i] or result[cur] == nums[i]: continue
#         is_used[i] = True
#         result[cur] = nums[i]
#         recur(cur+1)
#         is_used[i] = False

def recur(cur):
    if cur == M:
        print(*result)
        return
    
    prev = 0
    for i in range(N):
        if is_used[i] or prev == nums[i]: continue
        is_used[i] = True
        result[cur] = nums[i]
        prev = nums[i]
        recur(cur+1)
        is_used[i] = False

recur(0)
