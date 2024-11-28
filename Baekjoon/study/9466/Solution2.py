from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

T = int(input())

def dfs(cur):
    global team
    group.append(cur)
    check[cur] = True
    next = arr[cur]

    if not check[next]:
        dfs(next)
    else:
        if next in group:
            cycle_idx = group.index(next)
            team += group[cycle_idx:]

for _ in range(T):
    n = int(stdin.readline().rstrip())
    arr = [0] + list(map(int, stdin.readline().split()))
    check = [False] * (n+1)
    team = []
    
    for i in range(1, n+1):
        if not check[i]:
            group = []
            dfs(i)
    
    print(n-len(team))
