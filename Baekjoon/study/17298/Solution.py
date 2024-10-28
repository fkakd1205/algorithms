N = int(input())
arr = list(map(int, input().split()))
answer = [-1] * N
stack = []

for idx in range(N):
    if not stack:
        stack.append(idx)
        continue
    
    while stack and arr[stack[-1]] < arr[idx]:
        answer[stack.pop()] = arr[idx]
    
    stack.append(idx)

print(*answer)
