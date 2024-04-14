from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

# 1. 중위 순회 마지막 노드(end_node)를 구한다.
# 2. 중위 순회 마지막 노드에 방문할 때까지 cnt를 더해준다.
#    왕복 카운트를 더해야 하므로 end_node가 아닐 경우 한 번 더 더해준다.
N = int(input())
tree = [[] for _ in range(N+1)]
end_node = 0
cnt = 0
is_end_node = False

for _ in range(N):
    root, left, right = map(int, stdin.readline().split())
    tree[root] = [left, right]

def similar_in_order(node):
    global is_end_node
    global cnt

    if tree[node][0] != -1:
        cnt += 1
        similar_in_order(tree[node][0])
        if not is_end_node: cnt += 1
    
    if tree[node][1] != -1:
        cnt += 1
        similar_in_order(tree[node][1])
        if not is_end_node: cnt += 1

    if(node == end_node):
        is_end_node = True
        return

def in_order(node):
    global end_node

    if (tree[node][0] != -1):
        in_order(tree[node][0])
    end_node = node
    if (tree[node][1] != -1):
        in_order(tree[node][1])
        

in_order(1)
similar_in_order(1)
print(cnt)
