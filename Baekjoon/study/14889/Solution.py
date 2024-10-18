from sys import stdin

input = stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

is_used = [False] * N
mn = int(1e6)

def brute_force(cur, st):
    global mn
    if cur == N//2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if is_used[i] and is_used[j]:
                    start += arr[i][j]
                elif not is_used[i] and not is_used[j]:
                    link += arr[i][j]

        mn = min(mn, abs(start-link))
        return
    
    for i in range(st, N):
        if not is_used[i]:
            is_used[i] = True
            brute_force(cur+1, i+1)
            is_used[i] = False

brute_force(0, 0)
print(mn)
