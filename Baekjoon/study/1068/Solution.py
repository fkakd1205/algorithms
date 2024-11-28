from collections import deque

N = int(input())
parents = list(map(int, input().split()))
trees = [[] for _ in range(N)]
check = [False] * N
root_node = -1
answer = 0

for i in range(N):
    if parents[i] == -1:
        root_node = i
    else:
        trees[parents[i]].append(i)

rm_node = int(input().rstrip())

def remove_node(node):
    q = deque()
    check[node] = True
    q.append(node)

    while q:
        cur = q.popleft()

        for ad in trees[cur]:
            if check[ad]: continue
            check[ad] = True
            q.append(ad)

def search_leaf(node):
    global answer
    q = deque()
    q.append(node)
    while q:
        cur = q.popleft()
        child_cnt = 0

        for ad in trees[cur]:
            if check[ad]: continue
            child_cnt += 1
            check[ad] = True
            q.append(ad)

        if child_cnt == 0:
            answer += 1

# 노드 제거
remove_node(rm_node)

# 살아있는 leaf 노드 개수 확인
if check[root_node] == 0:
    search_leaf(root_node)

print(answer)
