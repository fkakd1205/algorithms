from sys import stdin

N, C = map(int, input().split())
house = [int(stdin.readline().rstrip()) for _ in range(N)]

house.sort()

st = 1
en = house[-1] - house[0]

while st <= en:
    cur = house[0]
    cnt = 1
    mid = (st + en) // 2

    for h in house:
        if cur + mid <= h:
            cur = h
            cnt += 1
    
    if cnt >= C:
        st = mid + 1
    else:
        en = mid - 1

print(st - 1)
