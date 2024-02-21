from sys import stdin
from collections import deque

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
q = deque([i for i in range(1, N+1)])

# V1.
# def left_shift(q, target):
#     shift_q = deque(q)
#     cnt = 0
#     while(shift_q[0] != target):
#         shift_q.append(shift_q.popleft())
#         cnt += 1

#     return shift_q, cnt

# def right_shift(q, target):
#     shift_q = deque(q)
#     cnt = 0
#     while(shift_q[0] != target):
#         shift_q.appendleft(shift_q.pop())
#         cnt += 1

#     return shift_q, cnt

# count = 0
# for target in nums:
#     if(q[0] == target):
#         q.popleft()
#     else:
#         left_shifted_q = left_shift(q, target)
#         right_shifted_q = right_shift(q, target)

#         if(left_shifted_q[1] > right_shifted_q[1]):
#             q = right_shifted_q[0]
#             count += right_shifted_q[1]
#         else:
#             q = left_shifted_q[0]
#             count += left_shifted_q[1]

#         q.popleft()

# print(count)

# V2. deque.index()로 target number의 위치를 찾는다
count = 0
for target in nums:
    while(target != q[0]):
        if(q.index(target) < (len(q) / 2)):
            q.append(q.popleft())
            count += 1
        else:
            q.appendleft(q.pop())
            count += 1

    q.popleft()

print(count)
