from sys import stdin

N, M = map(int, input().split())
point = [0] + [list(map(int, stdin.readline().split())) for _ in range(N)]
edges = []
parent = [i for i in range(N+1)]
result = 0

def get_dis(a, b):
    return ((point[a][0] - point[b][0]) ** 2 + (point[a][1] - point[b][1]) ** 2) ** 0.5

def find_p(x):
    if parent[x] != x:
        parent[x] = find_p(parent[x])
    return parent[x]

def union_p(x, y):
    x = find_p(x)
    y = find_p(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    union_p(a, b)

# 각 point 별로 거리를 구한다
for i in range(1, N):
    for j in range(i+1, N+1):
        d = get_dis(i, j)
        edges.append((d, i, j))

# 거리 오름차순 정렬
edges.sort()

# 거리가 가까운 것부터 같은 그룹으로 설정
# 크루스칼 알고리즘
for c, a, b in edges:
    if find_p(a) != find_p(b):
        union_p(a, b)
        result += c

print("{:.2f}".format(result))
