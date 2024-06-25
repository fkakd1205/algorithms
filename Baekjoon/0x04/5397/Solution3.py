from sys import stdin

n = int(input())

for _ in range(n):
    L = stdin.readline().rstrip()
    l_stack = []
    r_stack = []

    for chr in L:
        if chr == '<':
            if l_stack:
                r_stack.append(l_stack.pop())
        elif chr == '>':
            if r_stack:
                l_stack.append(r_stack.pop())
        elif chr == '-':
            if l_stack:
                l_stack.pop()
        else:
            l_stack.append(chr)

    r_stack.reverse()
    answer = ''.join([*l_stack, *r_stack])
    print(answer)
