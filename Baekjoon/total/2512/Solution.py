N = int(input())
costs = list(map(int, input().split()))
M = int(input())
costs.sort()

st = 1
en = costs[-1]
while st <= en:
    mid = (st + en) // 2
    cur = 0

    for cost in costs:
        if cost >= mid:
            cur += mid
        else:
            cur += cost
    
    if cur > M:
        en = mid - 1
    else:
        st = mid + 1

print(st - 1)
