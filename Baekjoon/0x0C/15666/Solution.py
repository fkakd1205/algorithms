from sys import stdin

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
arr = [0] * M

nums.sort()

def func(cur):
    if cur == M:
        result = []
        for i in range(M):
            result.append(nums[arr[i]])
        print(*result)
        return
    
    prev = 0
    start_idx = 0 if cur == 0 else arr[cur - 1]
    for i in range(start_idx, N):
        if prev == nums[i]: continue
        prev = nums[i]
        arr[cur] = i
        func(cur + 1)

func(0)
