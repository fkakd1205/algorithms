N, M = map(int, input().split())
arr = [0] * N

def func(cur):
    if cur == M:
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
        return
    
    st_idx = 1 if cur == 0 else arr[cur - 1]
    for i in range(st_idx, N+1):
        arr[cur] = i
        func(cur + 1)

func(0)
