from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
stack = []
result = []

for i in range(N):
    top = arr[i]
    
    while(stack and stack[-1][0] < top):
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][1])
    
    stack.append((top, i+1))

print(*result)
