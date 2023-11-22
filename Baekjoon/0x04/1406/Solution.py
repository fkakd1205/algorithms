# v1 - 시간초과
# N = list(input())
# cursor = len(N)

# M = int(input())

# for _ in range(M):
#     command = input().split()
    
#     if(command[0] == 'L'):
#         if(cursor > 0):
#             cursor -= 1
#     elif(command[0] == 'D'):
#         if(cursor < len(N)):
#             cursor += 1
#     elif(command[0] == 'B'):
#         if(cursor > 0):
#             N.pop(cursor-1)
#             cursor -= 1
#     else:
#         N.insert(cursor, command[1])
#         cursor += 1

# print(''.join(N))
    
# v2
from sys import stdin

N = list(input())
left_stack = N
right_stack = []

M = int(input())

for _ in range(M):
    command = list(stdin.readline().split())
    
    if(command[0] == 'L'):
        if(left_stack):
            value = left_stack.pop()
            right_stack.append(value)
    elif(command[0] == 'D'):
        if(right_stack):
            value = right_stack.pop()
            left_stack.append(value)
    elif(command[0] == 'B'):
        if(left_stack):
            left_stack.pop()
    else:
        left_stack.append(command[1])

left_stack.extend(reversed(right_stack))
print(''.join(left_stack))
