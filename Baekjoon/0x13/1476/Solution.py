from sys import stdin
from bisect import bisect_left

N = int(input())
A = list(map(int, stdin.readline().split()))
A.sort()

# V1. 시간 초과
# cnt = 0
# for i in range(N-2):    # 3명을 골라야하므로 N-3까지 확인
#     l_idx = i+1
#     r_idx = N-1

#     # 투포인터 + 이분탐색
#     while(l_idx < r_idx):
#         team = A[i] + A[l_idx] + A[r_idx]
#         if team > 0:
#             r_idx -= 1
#         else:
#             # 중복선택이 가능하므로, 중복되는 수 개수만큼 cnt를 증가시킨다.
#             if team == 0:
#                 if A[l_idx] == A[r_idx]:
#                     cnt += r_idx - l_idx
#                 else:
#                     duplic_idx = bisect_left(A, A[r_idx])
#                     cnt += r_idx - duplic_idx + 1
            
#             l_idx += 1

# print(cnt)

# V2.
def solve(st, en, team):
    global cnt
    while(st < en):
        temp = A[st] + A[en]
        if temp < team:
            st += 1
        elif temp > team:
            en -= 1
        else:
            if A[st] == A[en]:
                cnt += en - st
            else:
                duplic_idx = bisect_left(A, A[en])
                cnt += en - duplic_idx + 1
            st += 1

cnt = 0
for i in range(N-2):    # 3명을 골라야하므로 N-3까지 확인
    x = i+1
    y = N-1
    team = -A[i]

    solve(x, y, team)
print(cnt)