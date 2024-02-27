N, M = map(int, input().split())
arr = [0] * N

def func(cur):
    if cur == M:
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
        return
    
    for i in range(1, N+1):
        arr[cur] = i
        func(cur+1)

func(0)
