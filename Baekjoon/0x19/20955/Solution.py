from sys import stdin

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    p_x = find_parent(x)
    p_y = find_parent(y)

    if p_x < p_y:
        parent[p_y] = p_x
    else:
        parent[p_x] = p_y

# 사이클 끊는 횟수
cnt = 0
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    
    if find_parent(a) == find_parent(b):
        cnt += 1
    else:
        union_parent(a, b)

# 끊어진 뉴런 연결 횟수
link = 0
for i in range(1, N):
    if find_parent(i) != find_parent(i+1):
        union_parent(i, i+1)
        link += 1

print(cnt + link)
