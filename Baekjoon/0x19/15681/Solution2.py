from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
count = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(cur):
    count[cur] = 1

    for ad in tree[cur]:
        if count[ad] != 0: continue
        dfs(ad)
        count[cur] += count[ad]

dfs(R)

for _ in range(Q):
    q = int(stdin.readline().rstrip())
    print(count[q])
