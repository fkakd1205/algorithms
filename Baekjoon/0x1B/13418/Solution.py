from sys import stdin

N, M = map(int, input().split())
edges = [list(map(int, stdin.readline().split())) for _ in range(M+1)]
max_k = 0
min_k = 0

def find_p(x):
    if parent[x] != x:
        parent[x] = find_p(parent[x])
    return parent[x]

def union_p(x, y):
    x_p = find_p(x)
    y_p = find_p(y)

    if x_p < y_p:
        parent[y_p] = x_p
    else:
        parent[x_p] = y_p

# 0을 먼저 선택해 경로를 만드는 경우 (최악의 피로도)
parent = [i for i in range(N+1)]
edges.sort(key=lambda x: x[2])
for a, b, c in edges:
    if find_p(a) != find_p(b):
        union_p(a, b)
        if c == 0:
            max_k += 1

# 1을 먼저 선택해 경로를 만드는 경우 (최선의 피로도)
parent = [i for i in range(N+1)]
edges.sort(key=lambda x: -x[2])
for a, b, c in edges:
    if find_p(a) != find_p(b):
        union_p(a, b)
        if c == 0:
            min_k += 1

print(max_k**2 - min_k**2)
