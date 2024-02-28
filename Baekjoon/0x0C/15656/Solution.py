from sys import stdin

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
arr = [0] * M

nums.sort()

def func(cur):
    if cur == M:
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
        return

    for i in range(N):
        arr[cur] = nums[i]
        func(cur + 1)

func(0)
