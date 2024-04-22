from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

N, M = map(int, input().split())
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]
parent = [i for i in range(N+1)]
result = 0
last_c = 0

edges.sort(key= lambda x : x[2])

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

# 크루스칼 알고리즘
for a, b, c in edges:
    if find_p(a) != find_p(b):
        union_p(a, b)
        result += c
        last_c = c

# 이어진 최소 경로를 구하고, 마지막 경로를 끊는다
result -= last_c
print(result)
