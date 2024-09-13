from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

T = int(input())

def dfs(cur):
    global team

    check[cur] = True
    cycle.append(cur)

    next = students[cur]
    if not check[next]:
        dfs(next)
    else:
        # 사이클에 속한다면
        if next in cycle:
            team += cycle[cycle.index(next):]
        return

for _ in range(T):
    n = int(stdin.readline().rstrip())
    students = [0] + list(map(int, stdin.readline().split()))
    check = [False] * (n+1)
    team = []

    for i in range(1, n+1):
        if not check[i]:
            cycle = []
            dfs(i)

    print(n - len(team))
