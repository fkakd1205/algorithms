from sys import stdin

N, C = map(int, input().split())
arr = [int(stdin.readline().rstrip()) for _ in range(N)]
arr.sort()

# 이분탐색의 대상은 공유기 설치 최대 거리
st = 1
en = arr[-1] - arr[0]

while st <= en:
    mid = (st + en) // 2
    # 맨 앞에 공유기 설치
    cur = arr[0]
    cnt = 1

    for i in range(1, N):
        if arr[i] >= cur + mid:     # mid만큼 떨어진 공유기를 몇개 설치할 수 있나 확인
            cnt += 1
            cur = arr[i]

    if cnt >= C:
        st = mid + 1
    else:
        en = mid - 1

print(st - 1)
