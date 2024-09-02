from sys import stdin

T = int(input())

def make_postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    
    root = preorder[0]
    root_idx = inorder.index(root)
    l_inorder = inorder[:root_idx]
    r_inorder = inorder[root_idx+1:]
    l_preorder = preorder[1:len(l_inorder) + 1]
    r_preorder = preorder[len(l_inorder) + 1:]
    make_postorder(l_preorder, l_inorder)
    make_postorder(r_preorder, r_inorder)
    postorder.append(root)

for _ in range(T):
    n = int(input())
    postorder = []
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))
    make_postorder(preorder, inorder)
    print(*postorder)

