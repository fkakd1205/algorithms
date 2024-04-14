from sys import stdin
from collections import deque

N = int(input())
parents = list(map(int, stdin.readline().split()))
remove_node = int(input())
tree = [[] for _ in range(N)]
check = [False] * N
root_node = -1
cnt = 0

for i in range(len(parents)):
    p = parents[i]

    if p == -1:
        root_node = i
    else:
        tree[p].append(i)

def bfs():
    global cnt
    q = deque()
    q.append(root_node)
    check[root_node] = True

    if root_node == remove_node: return

    while q:
        cur = q.popleft()

        child_cnt = 0
        for child in tree[cur]:
            if check[child]: continue
            if (child == remove_node): continue
            check[child] = True
            q.append(child)
            child_cnt += 1
        
        if (child_cnt == 0): cnt += 1

bfs()
print(cnt)
