from sys import stdin, setrecursionlimit
# 파이썬 기본 재귀 깊이 제한 설정
setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    x, y = map(int, stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

# node와 연결된 다른 노드를 재귀 방문
# node와 연결된 다른 노드들의 parent를 node로 지정
def dfs(node):
    for i in tree[node]:
        if not parent[i]:
            parent[i] = node
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(parent[i])
