from sys import stdin

N, M, K = map(int, input().split())
arr = [0] + [int(stdin.readline().rstrip()) for _ in range(N)]
tree = [0] * (4*N+1)

def make_tree(x, left, right):
    if left == right:
        tree[x] = arr[left]
        return tree[x]

    mid = (left + right) // 2
    left_val = make_tree(2*x, left, mid)
    right_val = make_tree(2*x + 1, mid+1, right)
    tree[x] = left_val + right_val
    return tree[x]

def find_tree(x, st, en, left, right):
    if en < left or right < st:
        return 0
    
    if st <= left and right <= en:
        return tree[x]
    
    mid = (left + right) // 2
    left_val = find_tree(2*x, st, en, left, mid)
    right_val = find_tree(2*x + 1, st, en, mid+1, right)
    return left_val + right_val

def update_tree(x, idx, value, left, right):
    if left == right == idx:
        tree[x] = value
        return
    
    if idx < left or right < idx:
        return
    
    mid = (left + right) // 2
    update_tree(2*x, idx, value, left, mid)
    update_tree(2*x + 1, idx, value, mid+1, right)
    tree[x] = tree[2*x] + tree[2*x + 1]

make_tree(1, 0, N)

while M + K > 0:
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        update_tree(1, b, c, 0, N)
        M -= 1
    else:
        print(find_tree(1, b, c, 0 , N))
        K -= 1

