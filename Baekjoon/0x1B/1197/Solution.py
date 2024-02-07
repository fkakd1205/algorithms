from sys import stdin

V, E = map(int, input().split())
edges = []
for i in range(E):
    a, b, w = map(int ,stdin.readline().split())
    edges.append([w, a, b])
parent = [i for i in range(V+1)]
total_w = 0

edges.sort()

# find & union 알고리즘
def find_parent(x):
    if(parent[x] != x):
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)
    if(a_parent < b_parent):
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

# 크루스칼 알고리즘
for i in range (E):
    w, a, b = edges[i]
    # 다른 그룹인 경우 같은 그룹으로 합친다
    if(find_parent(a) != find_parent(b)):
        union_parent(a, b)
        total_w += w

print(total_w)
