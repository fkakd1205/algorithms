from sys import stdin, setrecursionlimit

setrecursionlimit(10**9)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_p = find(x)
    y_p = find(y)
    if x_p < y_p:
        parent[y_p] = x_p
    else:
        parent[x_p] = y_p        

for _ in range(M):
    c, a, b = map(int, stdin.readline().split())

    b_parent = find(b)
    a_parent = find(a)

    if c == 0:
        if a_parent != b_parent:
            union(a, b)
    else:
        if a_parent == b_parent:
            print("YES")
        else:
            print("NO")
        