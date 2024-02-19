from sys import stdin

s = input()
M = int(input())
left_stack = []
right_stack = []
cursor = len(s)

for i in s:
    left_stack.append(i)

for _ in range(M):
    command = stdin.readline().split()

    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

print(*left_stack, *reversed(right_stack), sep='')
