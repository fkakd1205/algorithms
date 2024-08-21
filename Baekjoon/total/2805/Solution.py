N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

st = 0
en = trees[-1]
while (st <= en):
    mid = (st + en) // 2
    h = 0

    for tree in trees:
        if tree > mid:
            h += tree - mid
        if h >= M:
            st = mid + 1
            break
    
    if h < M:
        en = mid - 1

print(st - 1)
