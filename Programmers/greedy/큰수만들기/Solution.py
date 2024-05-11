# V1. 시간초과
# from sys import setrecursionlimit
# setrecursionlimit(10**9)

# rm_cnt = 0
# num = ""
# mx = 0
# check = []

# def recur(cur):
#     global mx

#     if (sum(check) == rm_cnt or cur == len(num)):
#         result = ""
#         for i in range(len(num)):
#             if not check[i]:
#                 result += num[i]
#         mx = max(mx, int(result))
#         return
    
#     for i in range(len(num)):
#         if check[i]: continue
#         check[i] = True
#         recur(cur + 1)
#         check[i] = False

# def solution(number, k):
#     global rm_cnt, num, check
#     answer = ''
#     rm_cnt = k
#     num = number
#     check = [False] * (len(number))
#     recur(0)
#     answer = str(mx)
#     return answer

# V2. 스택
def solution(number, k):
    answer = ''
    answer_len = len(number) - k
    st = []

    for num in number:
        # 자신보다 작고, 제거 가능하다면 제거
        while (st and st[-1] < num and k > 0):
            st.pop()
            k -= 1
        st.append(num)
    
    for i in range(answer_len):
        answer += str(st[i])
    return answer

number = input()
k = int(input())
print(solution(number, k))