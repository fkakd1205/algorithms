N = int(input())

top = list(map(int, input().split()))
answer = [0] * N

stack = []

for i in range(N-1, -1, -1):
    if not stack:
        stack.append((top[i], i))
        continue

    while stack and stack[-1][0] < top[i]:
        _, idx = stack.pop()
        answer[idx] = i+1

    stack.append((top[i], i))

while stack:
    _, idx = stack.pop()
    answer[idx] = 0

print(*answer)
