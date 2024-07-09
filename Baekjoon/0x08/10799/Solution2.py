arr = input()
answer = 0
st = []

for i in range(len(arr)):
    if not st:
        st.append(arr[i])
        answer += 1
        continue

    if arr[i] == ')':
        # 레이저
        if arr[i-1] == '(':
            st.pop()
            answer += (len(st)-1)
        else:
            st.pop()
    else:
        st.append(arr[i])
        answer += 1

print(answer)
