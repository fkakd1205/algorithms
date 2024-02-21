from sys import stdin

T = int(input())

for _ in range(T):
    ps = stdin.readline().rstrip()
    st = []

    for a in ps:
        if not st:
            st.append(a)
        else:
            if ((a == ')' and st[-1] == '(')):
                st.pop()
            else:
                st.append(a)
    
    if st:
        print("NO")
    else:
        print("YES")
