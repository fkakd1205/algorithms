import sys

N = int(sys.stdin.readline())

for _ in range(N):
    L = list(sys.stdin.readline().rstrip())
    left_stack = []
    right_stack = []

    for command in L:
        if(command == '<'):
            if(left_stack):
                value = left_stack.pop()
                right_stack.append(value)
        elif(command == '>'):
            if(right_stack):
                value = right_stack.pop()
                left_stack.append(value)
        elif(command == '-'):
            if(left_stack):
                left_stack.pop()
        else:
            left_stack.append(command)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
