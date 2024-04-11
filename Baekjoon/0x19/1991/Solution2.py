from sys import stdin

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = stdin.readline().split()
    tree[root] = [left, right]

def pre_order(node):
    if node == '.': return
    print(node, end='')
    pre_order(tree[node][0])
    pre_order(tree[node][1])

def in_order(node):
    if node == '.': return
    in_order(tree[node][0])
    print(node, end='')
    in_order(tree[node][1])

def post_order(node):
    if node == '.': return
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end='')


pre_order('A')
print()

in_order('A')
print()

post_order('A')