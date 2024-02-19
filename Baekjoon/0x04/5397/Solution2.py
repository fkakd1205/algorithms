from sys import stdin

n = int(input())
passwords = [stdin.readline().rstrip() for _ in range(n)]

for pwd in passwords:
    left_stack = []
    right_stack = []

    for k in pwd:
        if k == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif k == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif k == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(k)

    print(*left_stack, *reversed(right_stack), sep="")
