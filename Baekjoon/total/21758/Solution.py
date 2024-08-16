from sys import stdin
from copy import deepcopy

# V1. 서브태스크 4 틀림
# N = int(input())
# honey = list(map(int, stdin.readline().split()))
# result = []

# def left_bottle():
#     for bee_idx in range(1, N-1):
#         s = sum(honey[:N-1]) - honey[bee_idx] + sum(honey[:bee_idx])
#         result.append(s)

# def right_bottle():
#     for bee_idx in range(1, N-1):
#         s = sum(honey[1:]) - honey[bee_idx] + sum(honey[bee_idx+1:])
#         result.append(s)

# def mid_bottle():
#     for bottle_idx in range(1, N-1):
#         s = sum(honey[1: bottle_idx+1]) + sum(honey[bottle_idx:N-1])
#         result.append(s)

# # 맨 왼쪽 - 벌통, 맨 오른쪽 - 벌 한마리 고정
# left_bottle()
# # 맨 왼쪽 - 벌 한마리, 맨 오른쪽 - 벌통 고정
# right_bottle()
# # 맨 왼쪽 - 별 한마리, 맨 오른쪽 - 벌 한마리 고정
# mid_bottle()
# print(max(result))

# V2.
N = int(input())
honey = list(map(int, stdin.readline().split()))
result = []

sum = deepcopy(honey)
for i in range(1, N):
    sum[i] += sum[i-1]

def left_bottle():
    for bee_idx in range(1, N-1):
        s = sum[N-2] - honey[bee_idx] + sum[bee_idx-1]
        result.append(s)

def right_bottle():
    for bee_idx in range(1, N-1):
        s = 2 * sum[N-1] - honey[0] - honey[bee_idx] - sum[bee_idx]
        result.append(s)

def mid_bottle():
    for bottle_idx in range(1, N-1):
        s = honey[bottle_idx] - honey[0] + sum[N-1] - honey[N-1]
        result.append(s)

# 맨 왼쪽 - 벌통, 맨 오른쪽 - 벌 한마리 고정
left_bottle()
# 맨 왼쪽 - 벌 한마리, 맨 오른쪽 - 벌통 고정
right_bottle()
# 맨 왼쪽 - 별 한마리, 맨 오른쪽 - 벌 한마리 고정
mid_bottle()
print(max(result))
