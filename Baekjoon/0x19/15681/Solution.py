from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
count = [0 for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)

def dfs(node):
    count[node] = 1
    for i in tree[node]:
        if not count[i]:
            dfs(i)
            count[node] += count[i]

dfs(R)

for _ in range(Q):
    U = int(stdin.readline())
    print(count[U])
