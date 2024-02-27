N, M = map(int, input().split())
isused = [False] * (N+1)
arr = [0] * N

def func(cur):
    if cur == M:
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
        return
    
    # 이전에 선택된 arr의 다음 숫자부터 for문 탐색
    st_idx = 1 if cur == 0 else arr[cur-1] + 1
    for i in range(st_idx, N+1):
        if isused[i]: continue
        arr[cur] = i
        isused[i] = True
        func(cur + 1)
        isused[i] = False
    
func(0)