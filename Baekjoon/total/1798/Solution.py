S = int(input())

st = 0
en = (S // 2) + 1

while(st <= en):
    mid = (st + en) // 2
    sum = (mid * (mid+1)) // 2

    if S >= sum:
        st = mid + 1
    else:
        en = mid - 1

print(st-1)