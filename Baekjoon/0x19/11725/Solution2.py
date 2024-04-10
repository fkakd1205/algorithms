from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

N = int(input())
adj = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(node):
    for ad in adj[node]:
        if parent[ad] != 0: continue
        parent[ad] = node
        dfs(ad)

parent[1] = -1     
dfs(1)

for i in range(2, N+1):
    print(parent[i])
