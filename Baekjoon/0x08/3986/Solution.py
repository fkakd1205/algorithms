from sys import stdin

N = int(input())
count = 0

for _ in range(N):
    command = stdin.readline().rstrip()
    stack = []

    for chr in command:
        if(len(stack) == 0):
            stack.append(chr)
        else:
            if(stack[len(stack)-1] == chr):
                stack.pop()
            else:
                stack.append(chr)

    if(len(stack) == 0):
        count += 1

print(count)
