from sys import stdin

N, M = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

# 선분의 왼쪽 점이 포함하는 최솟값의 점 인덱스
def left_point(cur):
    st = 0
    en = N - 1
    while st <= en:
        mid = (st + en) // 2
        if cur <= points[mid]:
            en = mid - 1
        else:
            st = mid + 1
    return en + 1

# 선분의 오른쪽 점이 포함하는 최대값 점 인덱스
def right_point(cur):
    st = 0
    en = N - 1
    while st <= en:
        mid = (st + en) // 2
        if cur >= points[mid]:
            st = mid + 1
        else:
            en = mid - 1
    return st - 1

for _ in range(M):
    l, r = map(int, stdin.readline().split())
    print(right_point(r) - left_point(l) + 1)
