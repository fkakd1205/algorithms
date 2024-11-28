from sys import stdin

N = int(input())
trees = {}

for _ in range(N):
    root, left, right = stdin.readline().split()
    trees[root] = [left, right]

def pre_order(cur):
    print(cur, end='')
    if trees[cur][0] != '.':
        pre_order(trees[cur][0])
    if trees[cur][1] != '.':
        pre_order(trees[cur][1])

def in_order(cur):
    if trees[cur][0] != '.':
        in_order(trees[cur][0])
    print(cur, end='')
    if trees[cur][1] != '.':
        in_order(trees[cur][1])

def post_order(cur):
    if trees[cur][0] != '.':
        post_order(trees[cur][0])
    if trees[cur][1] != '.':
        post_order(trees[cur][1])
    print(cur, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
