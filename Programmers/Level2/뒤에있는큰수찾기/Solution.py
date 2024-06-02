def solution(numbers):
    answer = []
    stack = []

    for i in range(len(numbers)-1, -1, -1):
        cur = numbers[i]

        if not stack or stack[-1] <= cur:
            while stack and stack[-1] <= cur: stack.pop()
        
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        
        stack.append(cur)
    return answer[::-1]

numbers = list(map(int, input().split()))
print(solution(numbers))
