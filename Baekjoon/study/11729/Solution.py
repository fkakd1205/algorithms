N = int(input())

def hanoi(n, st, mid, en):
    if n == 1:
        print(st, en)
        return
    
    # n-1개까지 a->b로 옮기기
    hanoi(n-1, st, en, mid)
    print(st, en)
    # 다 옮겨진 b에서 b->c로 옮긴다
    hanoi(n-1, mid, st, en)

K = 2 ** N - 1
print(K)
hanoi(N, 1, 2, 3)
