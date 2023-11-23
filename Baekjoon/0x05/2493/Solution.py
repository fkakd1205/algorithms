import sys

N = int(input())
top = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []

for i in range(N):
    while(stack):
        if(stack[-1][1] > top[i]):
            answer.append(stack[-1][0])
            break
        else:
            stack.pop()
    
    if not stack:
        answer.append(0)
    
    stack.append([i+1, top[i]])

print(' '.join(map(str, answer)))
