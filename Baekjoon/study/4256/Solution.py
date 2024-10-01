from sys import stdin

T = int(input())

def make_postorder(preorder, inorder):
    if not preorder:
        return
    
    root = preorder[0]
    idx = inorder.index(root)

    left_preorder = preorder[1:idx+1]
    right_preorder = preorder[idx+1:]
    left_inorder = inorder[0:idx]
    right_inorder = inorder[idx+1:]

    make_postorder(left_preorder, left_inorder)
    make_postorder(right_preorder, right_inorder)
    postorder.append(root)

for _ in range(T):
    postorder = []
    n = int(input())
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))
    make_postorder(preorder, inorder)
    print(*postorder)
