from sys import stdin

l_stack = list(input())
r_stack = []
k = int(input())

for i in range(k):
    command = list(stdin.readline().split())

    if command[0] == 'B':
        if l_stack:
            l_stack.pop()
    elif command[0] == 'L':
        if l_stack:
            r_stack.append(l_stack.pop())
    elif command[0] == 'D':
        if r_stack:
            l_stack.append(r_stack.pop())
    else:
        l_stack.append(command[1])

r_stack.reverse()
answer = [*l_stack, *r_stack]
print(''.join(answer))