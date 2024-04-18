# 위상정렬 X
# from sys import stdin

# N = int(input())
# M = int(input())
# prod = [[] for _ in range(N+1)]
# res = [0] * (N+1)

# for _ in range(M):
#     X, Y, K = map(int, stdin.readline().split())

#     prod[X].append((Y, K))

# for i in range(len(prod[N])):
#     Y, K = prod[N][i]
    
#     if not prod[Y]:
#         res[Y] += K
#     else:
#         for j in range(len(prod[Y])):
#             Y2, K2 = prod[Y][j]
#             res[Y2] += (K2 * K)

# while True:
#     flag = False
#     for i in range(1, N+1):
#         if (res[i] > 0 and len(prod[i]) != 0):
#             for j in range(len(prod[i])):
#                 Y2, K2 = prod[i][j]
#                 res[Y2] += (K2) * res[i]
#             res[i] = 0
#             flag = True

#     if not flag: break

# for i in range(1, N+1):
#     if res[i] > 0:
#         print(i, res[i])

# 위상정렬 이용
from sys import stdin
from collections import deque

N = int(input())
M = int(input())
prod = [[] for _ in range(N+1)]
indeg = [0] * (N+1)
cnt = [0] * (N+1)
is_base = [True] * (N+1)

for _ in range(M):
    X, Y, K = map(int, stdin.readline().split())

    is_base[X] = False
    prod[X].append((Y, K))
    indeg[Y] += 1   # 참조 횟수

q = deque()
q.append(N)
cnt[N] = 1  # 완제품은 1개 필요

while q:
    cur = q.popleft()

    for ad, c in prod[cur]:
        cnt[ad] += (c * cnt[cur])
        indeg[ad] -= 1
        if indeg[ad] == 0:
            q.append(ad)

for i in range(1, N+1):
    if is_base[i]:
        print(i, cnt[i])