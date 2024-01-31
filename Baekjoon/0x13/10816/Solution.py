from sys import stdin

N = int(input())
card = list(map(int, stdin.readline().split()))
M = int(input())
num = list(map(int, stdin.readline().split()))

card.sort()

# 정렬된 card에서 target이 들어갈 앞자리
def lower_idx(target):
    st = 0
    en = N
    while(st < en):
        mid = (st + en) // 2
        if(card[mid] >= target): en = mid
        else: st = mid + 1
    return st

# 정렬된 card에서 target이 들어갈 뒷자리
def upper_idx(target):
    st = 0
    en = N
    while(st < en):
        mid = (st + en) // 2
        if(card[mid] > target): en = mid
        else: st = mid + 1
    return st

result = []
for n in num:
    result.append(upper_idx(n) - lower_idx(n))

print(*result)
