from sys import stdin

# V1. 시간초과
# a = stdin.readline().rstrip()
# st = []
# laser_p = []  # 레이저 시작 인덱스를 담는 배열
# line = []     # 쇠막대기 (시작점, 끝점)을 담는 배열

# for i in range(len(a)):
#     cur = a[i]
    
#     if not st:
#         st.append(i)
#     else:
#         if (cur == ')' and a[st[-1]] == '('):
#             if(st[-1] == i-1):
#                 laser_p.append(st.pop())
#             else:
#                 # 막대기의 시작점과 끝점을 넣는다
#                 line.append((st.pop(), i))
#         else:
#             st.append(i)

# sum = 0
# for st, en in line:
#     count = 1
#     for i in laser_p:
#         if(st < i < en):
#             count += 1
#     sum += count

# print(sum)

# V2
a = stdin.readline().rstrip()
st = []
count = 0

for i in range(len(a)):
    cur = a[i]

    if cur == '(':
        st.append(cur)
    else:
        # 레이저 발견
        if a[i-1] == '(':
            st.pop()
            count += len(st)
        else:
            st.pop()
            count += 1

print(count)
