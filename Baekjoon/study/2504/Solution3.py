brackets = list(input().rstrip())
st = []
mul = 1
answer = 0

for i in range(len(brackets)):
    b = brackets[i]
    if b == '(':
        st.append('(')
        mul *= 2
    elif b == '[':
        st.append('[')
        mul *= 3
    elif b == ')':
        if st and st[-1] == '(':
            if brackets[i-1] == '(':
                answer += mul
            mul //= 2
            st.pop()
        else:
            answer = 0
            break
    else:
        if st and st[-1] == '[':
            if brackets[i-1] == '[':
                answer += mul
            mul //= 3
            st.pop()
        else:
            answer = 0
            break

if st:
    answer = 0
    
print(answer)
