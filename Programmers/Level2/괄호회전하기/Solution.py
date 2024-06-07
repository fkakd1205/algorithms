from collections import deque

def is_match(st, br):
    if not st or st[-1] != br:
        return False
    return True

def solution(s):
    answer = 0
    size = len(s)
    q = deque(s)

    for _ in range(size):
        stack = []
        for bracket in q:
            if not stack:
                stack.append(bracket)
                continue
            if bracket == ']':
                if not is_match(stack, '['):
                    break
                else:
                    stack.pop()
            elif bracket == ')':
                if not is_match(stack, '('):
                    break
                else:
                    stack.pop()
            elif bracket == '}':
                if not is_match(stack, '{'):
                    break
                else:
                    stack.pop()
            else:
                stack.append(bracket)

        if not stack: answer += 1
        q.append(q.popleft())
    return answer

s = input()
print(solution(s))
