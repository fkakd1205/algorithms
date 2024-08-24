from sys import stdin

N, M = map(int, input().split())
times = [int(stdin.readline().rstrip()) for _ in range(N)]
times.sort()

st = times[0]
en = times[-1] * M

while st <= en:
    mid = (st + en) // 2
    cnt = 0

    # mid 시간 동안 cnt 명의 사람이 심사받을 수 있다
    for t in times:
        cnt += mid // t

    if cnt >= M:
        en = mid - 1
    else:
        st = mid + 1

print(en + 1)
