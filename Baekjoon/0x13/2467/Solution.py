from sys import stdin

MX = int(2e9)
N = int(input())
liquid = list(map(int, stdin.readline().split()))

mn = MX
l_idx = 0
result = tuple()

for i in range(N-1):
    cur = liquid[i]

    # i번째 용액과 i+1 ~ N-1 번째 용액들의 값 차이를 이분탐색으로 확인
    st = i+1
    en = N-1
    while (st <= en):
        mid = (st + en) // 2
        temp = cur + liquid[mid]

        if abs(temp) < mn:
            mn = abs(temp)
            result = (liquid[i], liquid[mid])

        if temp == 0:
            break
        elif temp < 0:
            st = mid + 1
        else:
            en = mid - 1

print(*result)
