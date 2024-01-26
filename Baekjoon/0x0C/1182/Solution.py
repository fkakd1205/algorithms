# 풀이1
# from sys import stdin

# N, S = map(int, input().split())
# number = list(map(int, stdin.readline().split()))
# count = 0

# def func(cur, sum):
#     if cur == N:
#         if sum == S:
#             global count
#             count += 1
#     else:
#         # 다른 원소를 더하지 않는 경우, 더하는 경우
#         func(cur + 1, sum)
#         func(cur + 1, sum + number[cur])

# func(0, 0)

# if(S == 0):
#     print(count - 1)    # 공집합인 경우
# else:
#     print(count)

# 풀이2 - itertools의 combinations사용
from sys import stdin
from itertools import combinations

N, S = map(int, input().split())
number = list(map(int, stdin.readline().split()))
count = 0

for i in range(1, N+1):
    comb = combinations(number, i)

    for num in comb:
        if sum(num) == S:
            count += 1

print(count)
