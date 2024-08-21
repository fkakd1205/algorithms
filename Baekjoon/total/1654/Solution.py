from sys import stdin

N, K = map(int, input().split())
lines = [int(stdin.readline().rstrip()) for _ in range(N)]

st = 1
en = max(lines)
while(st <= en):
    mid = (st + en) // 2
    cnt = 0

    for line in lines:
        cnt += line // mid
        if cnt >= K:
            st = mid + 1
            break

    if cnt < K:
        en = mid - 1

print(st-1)
