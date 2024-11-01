store = list(input().rstrip())
bomb = list(input().rstrip())

stack = []

for chr in store:
    stack.append(chr)
    if stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(*stack, sep="")
