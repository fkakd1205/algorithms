N,M = map(int, input().split())

num = [0] * M
is_used = [False] * (N+1)

def recur(cur):
    if cur == M:
        print(*num)
        return

    for i in range(1, N+1):
        if is_used[i]: continue
        is_used[i] = True
        num[cur] = i
        recur(cur+1)
        is_used[i] = False

recur(0)
