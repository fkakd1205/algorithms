n, k = map(int, input().split())

st = 0
en = n
answer = "NO"

# 총 나눠진 종이 수 = (가로 cut + 1) * (세로 cut + 1)
while st <= en:
    # mid = 가로 cut
    mid = (st + en) // 2
    
    # 세로 cut = n - 가로 cut
    cnt = (mid + 1) * (n - mid + 1)
    if cnt == k:
        answer = "YES"
        break
    elif cnt > k:
        en = mid - 1
    else:
        st = mid + 1

print(answer)
