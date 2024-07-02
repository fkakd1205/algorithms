N = int(input())
A = list(map(int, input().split()))

st = []
answer = [-1] * N

for idx, num in enumerate(A):
    if not st:
        st.append((idx, num))
        continue
    
    if st[-1][1] >= num:
        st.append((idx, num))
        continue

    while st and st[-1][1] < num:
        index, _ = st.pop()
        answer[index] = num
    
    st.append((idx, num))

print(*answer)
    