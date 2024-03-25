from sys import stdin
from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, stdin.readline().split()))
cards.sort()

M = int(input())
target = list(map(int, stdin.readline().split()))
result = []

for i in range(M):
    st = bisect_left(cards, target[i])
    en = bisect_right(cards, target[i])

    # 찾아진 위치의 첫번째 값이 N보다 작고
    # 해당 카드의 값이 target 값과 동일하다면
    if st < N and target[i] == cards[st]:
        result.append(en - st)
    else:
        result.append(0)

print(*result)
