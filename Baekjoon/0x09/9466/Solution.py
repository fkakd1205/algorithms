from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

T = int(input())

def dfs(n):
    global team
    visited[n] = True
    cycle.append(n)
    next_n = S[n]

    # 이미 visited된 곳이라면
    if visited[next_n]:
        # 현재 생성된 경로에 next_n이 포함된다면 사이클이 생긴것이다
        if next_n in cycle:
            # cycle이 생긴 지점부터 팀이 된다
            team += cycle[cycle.index(next_n):]
        return
    else:
        dfs(next_n)

for _ in range(T):
    n = int(input())
    S = [0] + list(map(int, stdin.readline().split()))
    visited = [False] * (n+1)
    team = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    
    print(n - len(team))
