N = int(input())
heights = [0] + list(map(int, input().split()))
stack = []
answer = []

for i in range(1, N+1):
    # 자신보다 작은 높이의 탑들 제거
    while stack and heights[i] > heights[stack[-1]]:
        stack.pop()

    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1])

    stack.append(i)

print(*answer)
