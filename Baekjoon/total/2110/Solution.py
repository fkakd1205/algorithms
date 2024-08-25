from sys import stdin

N, C = map(int, input().split())
locations = [int(stdin.readline().rstrip()) for _ in range(N)]
locations.sort()

st = 1
en = locations[-1] - locations[0]
while st <= en:
    mid = (st + en) // 2    # 두 공유기 사이 최대 거리
    cur = locations[0]
    cnt = 1
    
    # C개 이상의 공유기를 설치할 수 있으면 두 공유기 사이 최대 거리로 mid가 가능
    for i in range(1, N):
        if locations[i] >= cur + mid:
            cur = locations[i]
            cnt += 1
    
    if cnt >= C:
        st = mid + 1
    else:
        en = mid - 1

print(st - 1)
