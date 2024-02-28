from sys import stdin

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
isused = [False] * N
arr = [0] * M

nums.sort()

def func(cur):
    if cur == M:
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
        return

    prev = 0
    for i in range(N):
        # 오름차순 정렬되었으니, 바로 이전의 값과 동일하지 않으면 된다
        if not isused[i] and prev != nums[i]:
            isused[i] = True
            arr[cur] = nums[i]
            prev = nums[i]
            func(cur + 1)
            isused[i] = False

func(0)
