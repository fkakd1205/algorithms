N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

is_used = [False] * N
result = [-1] * M

def recur(cur):
    if cur == M:
        print(*result)
        return
    
    for i in range(N):
        if is_used[i]: continue
        is_used[i] = True
        result[cur] = arr[i]
        recur(cur + 1)
        is_used[i] = False

recur(0)
