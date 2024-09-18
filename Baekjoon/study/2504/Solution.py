bracket = input()
stack = []
answer = 0
temp = 1

for i in range(len(bracket)):
    # bracket[i-1]이 현재 괄호와 매칭되는 경우메만, answer에 더해준다.
    if bracket[i] == '(':
        stack.append(bracket[i])
        temp *= 2
    elif bracket[i] == '[':
        stack.append(bracket[i])
        temp *= 3
    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if bracket[i-1] == '(':
            answer += temp
        
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if bracket[i-1] == '[':
            answer += temp

        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)