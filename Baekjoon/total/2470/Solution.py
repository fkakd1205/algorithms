N = int(input())
arr = list(map(int, input().split()))
arr.sort()
INF = int(2e9)
answer = tuple()

st = 0
en = len(arr) - 1
mn = INF

# 투포인터
while st < en:
    sum = arr[st] + arr[en]
    if abs(sum) < mn:
        mn = abs(sum)
        answer = (arr[st], arr[en])

    if sum >= 0:
        en -= 1
    else:
        st += 1

print(*answer)
