from sys import stdin

N, M = map(int, input().split())
line = list(map(int, input().split()))

# 미리 정렬!
line.sort()

def search_left(target):
    st = 0
    en = N-1

    while st <= en:
        mid = (st + en) // 2
        
        if target <= line[mid]:
            en = mid - 1
        else:
            st = mid + 1
    return en + 1

def search_right(target):
    st = 0
    en = N-1

    while st <= en:
        mid = (st + en) // 2

        if target >= line[mid]:
            st = mid + 1
        else:
            en = mid - 1
    return st - 1

for _ in range(M):
    left, right = map(int, stdin.readline().split())
    print(search_right(right) - search_left(left) + 1)
