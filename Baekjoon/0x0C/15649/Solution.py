N, M = map(int, input().split())
arr = [0] * (N+1)
isused = [0] * (N+1)

def func(cur):
    if(cur == M):
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
    else:
        for i in range(1, N+1):
            # i가 수열에 포함되지 않는다면
            if not isused[i]:
                arr[cur] = i
                isused[i] = 1
                func(cur+1)
                isused[i] = 0

func(0)
