from sys import stdin

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
result = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

# 부모 찾기
def find_p(a):
    if parent[a] != a:
        parent[a] = find_p(parent[a])
    return parent[a]

# 그룹 합치기
def union_p(a, b):
    a_p = find_p(a)
    b_p = find_p(b)

    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

for c, a, b in edges:
    # 가중치가 작은 것부터 확인
    # 두 edge가 다른 그룹인 경우 같은 그룹으로 합친다
    if (find_p(a) != find_p(b)):
        union_p(a, b)
        result += c

print(result)
