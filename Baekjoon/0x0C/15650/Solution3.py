N, M = map(int, input().split())
arr = [0] * M

def recur(cur, st):
    if cur == M:
        print(*arr)
        return
    
    for i in range(st, N+1):
        arr[cur] = i
        recur(cur + 1, i + 1)

recur(0, 1)
