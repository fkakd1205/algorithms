from sys import stdin

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
arr = [0] * M
isused = [False] * N

nums.sort()

def func(cur):
    if cur == M:
        result = []
        for i in range(M):
            result.append(nums[arr[i]])
        print(*result)
        return
    
    start_idx = 0 if cur == 0 else arr[cur-1] + 1
    for i in range(start_idx, N):
        if isused[i]: continue
        arr[cur] = i
        isused[i] = True
        func(cur + 1)
        isused[i] = False

func(0)