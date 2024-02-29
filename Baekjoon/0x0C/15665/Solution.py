from sys import stdin

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
arr = [0] * M

nums.sort()

def func(cur):
    if cur == M:
        print(*arr)
        return
    
    prev = 0
    for i in range(N):
        if prev == nums[i]: continue
        arr[cur] = nums[i]
        prev = nums[i]
        func(cur + 1)

func(0)
