from sys import stdin

N = int(input())
tree = {}

def pre_order(parent):
    if parent != '.':
        print(parent, end='')
        pre_order(tree[parent][0])
        pre_order(tree[parent][1])

def in_order(parent):
    if parent != '.':
        in_order(tree[parent][0])
        print(parent, end='')
        in_order(tree[parent][1])

def post_order(parent):
    if parent != '.':
        post_order(tree[parent][0])
        post_order(tree[parent][1])
        print(parent, end='')

for _ in range(N):
    parent, left, right = stdin.readline().split()
    tree[parent] = (left, right)

pre_order('A')
print()

in_order('A')
print()

post_order('A')
print()

