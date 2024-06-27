from sys import stdin

n = int(input())
st = []
answer = []
cur = 1

for i in range(n):
    target = int(stdin.readline().rstrip())

    while(cur <= target):
        st.append(cur)
        cur += 1
        answer.append('+')

    if st[-1] == target:
        st.pop()
        answer.append('-')
    else:
        break

if st:
    print("NO")
else:
    print(*answer, sep="\n")
