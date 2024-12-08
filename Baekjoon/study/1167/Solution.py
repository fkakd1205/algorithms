from sys import stdin, setrecursionlimit

INF = int(1e9)
setrecursionlimit(10 ** 9)
N = int(input())
trees = [[] for _ in range(N+1)]
answer = 0

for _ in range(N):
    tree = list(map(int, stdin.readline().split()))
    idx = 1

    while tree[idx] != -1:
        trees[tree[0]].append((tree[idx], tree[idx+1]))
        idx += 2

def dfs(cur, cost):
    checked[cur] = cost

    for ad, c in trees[cur]:
        if checked[ad] == -1:
            dfs(ad, cost + c)
            
def search_far_node():
    st = -1
    mx = -1
    for i in range(1, N+1):
        if checked[i] > mx:
            mx = checked[i]
            st = i

    return st

# 임의의 점에서 가장 먼 노드 A, 그리고 A에서 가장 먼 노드 B를 찾고
# A - B 거리가 트리의 지금
checked = [-1] * (N+1)
dfs(1, 0)
node = search_far_node()

checked = [-1] * (N+1)
dfs(node, 0)
print(checked[search_far_node()])
