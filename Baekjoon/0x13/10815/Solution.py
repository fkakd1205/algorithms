from sys import stdin
from bisect import bisect_left

N = int(input())
card = list(map(int, stdin.readline().split()))
M = int(input())
num = list(map(int, stdin.readline().split()))

card.sort()

result = []
for n in num:
    # bisect_left를 사용해 이진탐색 진행. target_idx는 n이 삽입될 첫번째 인덱스를 찾는다.
    target_idx = bisect_left(card, n)
    if(target_idx < len(card) and card[target_idx] == n):
        result.append(1)
    else:
        result.append(0)

print(*result)
