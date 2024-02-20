from sys import stdin

K = int(input())
stack = []

for _ in range(K):
    n = int(stdin.readline().rstrip())
    if(n == 0):
        if stack:
            stack.pop()
    else:
        stack.append(n)

print(sum(stack))
